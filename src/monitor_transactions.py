import pandas as pd

def load_transaction_data(file_path):
    """Loads transaction data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        # print(f"Successfully loaded {len(df)} rows from {file_path}")
        # print("First 5 rows:")
        # print(df.head())
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

    # Placeholder for future checks (akan diisi di commit berikutnya)
    # if df['transaction_id'].duplicated().any():
    #     issues_found.append("Duplicate transaction_id found.")

    # if (df['amount'] <= 0).any():
    #     issues_found.append("Non-positive amount found.")

    # valid_types = ['SEND', 'RECEIVE', 'TOPUP', 'TRANSFER', 'PAYMENT']
    # if not df['transaction_type'].isin(valid_types).all():
    #     issues_found.append("Invalid transaction_type found.")

    print("--- Missing values check complete ---")

    return issues_found

if __name__ == "__main__":
    # Path to your raw transactions data
    raw_data_path = '../data/raw/transactions.csv'

    all_issues = run_data_quality_checks(raw_data_path)

    if all_issues:
        print("\n!!! DATA QUALITY ISSUES DETECTED !!!")
        for issue in all_issues:
            print(f"- {issue}")
    else:
        print("\nAll primary data quality checks passed. Data looks good!")
    print("--- Checks Complete ---")