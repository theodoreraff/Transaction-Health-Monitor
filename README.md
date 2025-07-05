# Transaction-Health-Monitor

## 📊 Project Overview
This project demonstrates an automated Python-based system for monitoring the data quality of simulated digital wallet transactions. It aims to ensure the accuracy, completeness, and reliability of financial transaction data, which is critical for fintech operations and fraud prevention.

## ✨ Features
-   **Data Loading:** Reads transaction data from a CSV file.
-   **Missing Values Check:** Identifies missing values in critical transaction columns.
-   **Unique ID Validation:** Verifies the uniqueness of transaction IDs.
-   **Positive Amount Check:** Ensures all transaction amounts are positive and numeric.
-   **Valid Type Check:** Validates transaction types against a predefined list.
-   **Console Reporting:** Provides a clear summary of detected data quality issues.

## 🛠️ Technologies Used
-   Python 3.x
-   Pandas (for data manipulation and analysis)

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/theodoreraff/Transaction-Health-Monitor.git](https://github.com/theodoreraff/Transaction-Health-Monitor.git) # Ganti dengan link repo kamu
    cd Transaction-Health-Monitor
    ```
2.  **Ensure data is present:** Make sure `transactions.csv` is located in the `data/raw/` directory.
3.  **Run the script:**
    ```bash
    python src/monitor_transactions.py
    ```
    The data quality report will be printed to the console.

## 💡 Future Enhancements
-   Integrate with a database (e.g., SQLite/PostgreSQL) for storing raw and processed data.
-   Implement automated scheduling using Apache Airflow or cron jobs.
-   Develop more sophisticated reporting (e.g., HTML reports, email notifications).
-   Add advanced data quality checks (e.g., timestamp validation, cross-field consistency).
-   Containerize the application using Docker.