 # 📊 Vendor Performance Analysis | SQL • Python • Power BI

 ## This project presents an end-to-end Vendor Performance Analysis pipeline built using SQLite, Python, and Power BI.
It evaluates vendor profitability, pricing efficiency, inventory turnover, bulk-purchase advantages, high-margin low-sales brands, and vendor dependency risks using integrated retail datasets.

The project includes data ingestion, EDA, summary table creation, statistical analysis, and a fully interactive **Power BI Dashboard**.

 # 📁 Dataset

All raw data tables used in this project are available here:

🔗 Google Drive (Data Files):
https://drive.google.com/drive/folders/1erbLbZfkdrBo5fBNuPR1sFVMkdXnivg7

 # 📌 Project Workflow
 ## 1️⃣ Data Ingestion (SQLite + Python)

 * Imported begin_inventory, end_inventory, purchases, purchase_prices, sales, and vendor_invoice tables into inventory.db.

 * Validated schema, handled null values, removed duplicates, and created indexes for performance improvement.

 * Scripts included: ingestion_db.py, ingestion.ipynb

 ## 2️⃣ Exploratory Data Analysis (Python)

**Performed extensive EDA to understand**:

 * Pricing variation

 * Purchase & sales quantities

 * Excise tax and freight cost behavior

 * Profit distribution, turnover, and outliers

**Visualizations include**:

 * Box plots for numerical columns

 * Correlation heatmaps

 * Scatter plots and distribution charts

**Notebook**:
📄 Exploratory Data Analysis.ipynb

 ## 3️⃣ Summary Table Creation

**Built a consolidated vendor_sales_summary table that merges**:

 * Purchase data

 * Sales data

 * Freight costs

 * Product pricing

 * Profit metrics

**Includes derived fields like**:

 * Gross Profit

 * Profit Margin

 * Stock Turnover

 * Sales-to-Purchase Ratio

 * Unsold Capital

**Script**:
📄 get_vendor_summary.py

**Export**:
📄 vendor_sales_summary.csv

 ## 4️⃣ Statistical Analysis & Business Insights

**Using the summary table, the project uncovered**:

 * High-margin but low-sales brands (198 brands)
 * Strong vendor dependency (Top 10 vendors = 65.69% of purchases)
 * 72% cost reduction via bulk purchasing
 * Unsold inventory capital worth $2.71M
 * Clear profitability differences validated using hypothesis testing

 * All findings are documented in:
📄 Vendor Performance Analysis Project Report.pdf

 ## 5️⃣ Power BI Dashboard

A fully interactive dashboard was created from the vendor_sales_summary table, containing:

**KPI Cards**

 * Total Sales

 * Total Purchase

 * Gross Profit

 * Avg Profit Margin

 * Total Unsold Capital (DAX measure)

**Key Visuals**

 * **Donut Chart**: Vendor Purchase Contribution%

 * **Bar Chart**: Top Vendors by Sales

 * **Bar Chart**: Top Brands by Sales

 * **Funnel**: Low-Performing Vendors (Stock Turnover < 1)

 * **Scatter Plot**: Low-Performing Brands (low sales, high margins)

**Dashboard File**:
📊 Vendor Performance Analysis Dashboard.pbix

**Layout Preview**:
🖼 Vendor Performance Dashboard Layout.png

 ## 🛠️ Technologies Used

 * Python (Pandas, NumPy, Matplotlib, SQLite3)

 * SQL (SQLite)

 * Power BI (DAX, interactive visuals)

  * Jupyter Notebooks

## 🚀 Key Outcomes

 * Unified multi-table retail data into a single analytical summary table

 * Identified critical vendor and brand performance patterns

 * Built an enterprise-ready Power BI dashboard

Delivered data-driven recommendations to improve profitability

## 📧 Contact

If you’d like help improving the dashboard, optimizing DAX, or expanding analysis—just ask!
