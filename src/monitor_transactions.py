import pandas as pd

def load_transaction_data(file_path):
    """Loads transaction data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None

def run_data_quality_checks(file_path):
    """Runs a series of data quality checks on the transaction data."""
    df = load_transaction_data(file_path)
    if df is None:
        return []

    issues_found = []
    print(f"--- Running Data Quality Checks for {file_path} ---")

    # 1. Check for Missing Values in critical columns
    critical_columns = ['transaction_id', 'user_id', 'amount', 'transaction_type', 'timestamp']
    for col in critical_columns:
        if df[col].isnull().any():
            issues_found.append(f"Missing values detected in column: '{col}'")
            print(f"  Issue: Missing values in '{col}'")

    # 2. Check for Unique Transaction IDs
    if 'transaction_id' in df.columns and df['transaction_id'].duplicated().any():
        issues_found.append("Duplicate 'transaction_id' found.")
        print("  Issue: Duplicate 'transaction_id' detected.")

    print("--- Unique transaction ID check complete ---")

    return issues_found

if __name__ == "__main__":
    raw_data_path = 'data/raw/transactions.csv'
    all_issues = run_data_quality_checks(raw_data_path)

    if all_issues:
        print("\n!!! DATA QUALITY ISSUES DETECTED !!!")
        for issue in all_issues:
            print(f"- {issue}")
    else:
        print("\nAll primary data quality checks passed. Data looks good!")
    print("--- All Checks Complete ---")