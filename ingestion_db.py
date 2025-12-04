import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time

# -------------------------------------------------------------------
# Logging configuration
# -------------------------------------------------------------------
logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

# -------------------------------------------------------------------
# DB engine and data directory setup (from Cell 2)
# -------------------------------------------------------------------
# Show where the notebook is running
print("Current working directory:", os.getcwd())

# Create SQLite engine (creates inventory.db in this folder if it doesn't exist)
engine = create_engine("sqlite:///inventory.db")
print("SQLite engine created for inventory.db")

# Folder that contains your CSV files
data_dir = "data"
print("Data directory set to:", data_dir)

# Check that the folder exists and list files
if os.path.isdir(data_dir):
    print(f"Contents of '{data_dir}':", os.listdir(data_dir))
else:
    print(f"WARNING: Directory '{data_dir}' does NOT exist!")

# -------------------------------------------------------------------
# ingest_db function (from Cell 3)
# -------------------------------------------------------------------
def ingest_db(csv_path: str, table_name: str, engine):
    """
    Read a CSV in chunks and save to SQLite, splitting further
    to avoid SQLite's 'too many SQL variables' limit, with minimal output.
    """
    print(f"Starting ingest for: {csv_path} -> table '{table_name}'")

    # Rows to read from CSV at a time (controls RAM usage)
    read_chunksize = 50_000

    # Stay below SQLite's default max variable limit (usually 999)
    max_sql_variables = 900

    first_write = True
    total_rows = 0

    # Read the CSV in chunks
    for chunk in pd.read_csv(csv_path, chunksize=read_chunksize):
        num_cols = len(chunk.columns)
        # Max rows per batch so that rows * columns <= max_sql_variables
        rows_per_batch = max(1, max_sql_variables // num_cols)

        # Split the chunk into smaller batches and write each
        for start in range(0, len(chunk), rows_per_batch):
            batch = chunk.iloc[start:start + rows_per_batch]

            batch.to_sql(
                table_name,
                engine,
                if_exists="replace" if first_write else "append",
                index=False
            )

            first_write = False
            total_rows += len(batch)

    print(f"Finished ingest for: {table_name} (total rows written: {total_rows})")

# -------------------------------------------------------------------
# load_raw_data function (updated Cell 4 with logging)
# -------------------------------------------------------------------
def load_raw_data():
    """This function will load the CSVs and ingest them into the database."""
    data_dir = "data"

    start = time.time()
    logging.info("Scanning data directory '%s' for CSV files...", data_dir)

    if not os.path.isdir(data_dir):
        logging.error("Directory '%s' does not exist. Fix data_dir or create the folder.", data_dir)
        return

    files = os.listdir(data_dir)
    logging.info("All files in '%s': %s", data_dir, files)

    processed_any = False

    for file in files:
        # Only handle CSV files
        if file.lower().endswith(".csv"):
            processed_any = True
            csv_path = os.path.join(data_dir, file)
            table_name = file[:-4]  # strip ".csv" from filename

            logging.info("Ingesting '%s' into db as table '%s'...", file, table_name)

            try:
                ingest_db(csv_path, table_name, engine)
            except PermissionError as e:
                logging.warning(
                    "PermissionError while accessing '%s': %s. "
                    "Tip: Close this file in Excel or any other program and rerun.",
                    csv_path,
                    e
                )
            except Exception as e:
                # Log full stack trace for unexpected errors
                logging.exception("Error while ingesting '%s': %s", csv_path, e)

    end = time.time()
    total_time = (end - start) / 60

    if not processed_any:
        logging.warning("No CSV files found to process. Check filenames and filters.")
    else:
        logging.info("-- Ingestion Complete --")
        logging.info("Total Time Taken: %.2f minutes", total_time)

# -------------------------------------------------------------------
# Main guard
# -------------------------------------------------------------------
if _name_ == "_main_":
    load_raw_data()