# SME Expansion Analytics: Customer Return & Root Cause Analysis

## 📌 Business Overview
An e-commerce business recently expanded its operations across European markets (Italy, Spain, Germany, France). While revenue increased, management raised concerns over a sudden spike in product returns and customer churn. 
This project combines quantitative data (transactional records) and qualitative data (unstructured customer support tickets) to pinpoint the financial impact and root causes of these returns, bridging the gap between raw data and international market dynamics.

## 🛠️ Tech Stack
* **SQL:** Data extraction, aggregation, and KPI calculations (Return Rates, Order Volumes).
* **Python (Pandas):** Data manipulation, relational merging, and text processing (NLP-inspired tagging) for root cause analysis.

## 🚀 Methodology & Workflow

### Phase 1: Quantitative Analysis (SQL)
* Processed transactional records to calculate Total Orders, Returned Orders, and Return Rate Percentages across various countries and product categories.
* **Key Finding:** Identified a critical bottleneck in **Spain**, specifically within the **Electronics** category, which exhibited a highly disproportionate return rate compared to the baseline.

### Phase 2: Qualitative Analysis (Python)
* Merged structured order data with unstructured customer support tickets (`INNER JOIN` logic in Pandas).
* Engineered a custom text-processing function to scan and categorize customer complaints based on recurring semantic patterns.
* **Key Finding:** Discovered that the high return rate in Spain was not due to product quality or buyer's remorse, but primarily driven by **Packaging & Physical Damage** (e.g., "crushed box", "broken item") during transit.

## 💡 Actionable Business Insights
1. **Logistics Optimization:** Immediate redesign of packaging protocols for fragile electronics shipped to Spain is required to minimize transit damage.
2. **Cost Recovery & Vendor Management:** The business must evaluate and potentially renegotiate terms with the regional shipping vendor in Spain, as logistics failures are directly inflating operational costs and driving customer churn.

## 📂 Repository Structure
* `Data_Extraction.sql`: SQL queries used to aggregate sales data and isolate high-risk market segments.
* `Root_Cause_Analysis.py`: Python script utilizing Pandas to merge datasets and parse text for complaint categorization.
* `Transactions.csv` & `Customer_Tickets.csv`: Simulated datasets used for the analysis.
