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

    # 3. Check for Positive Amount
    if 'amount' in df.columns:
        # Ensure 'amount' is numeric for comparison, errors will turn non-numeric into NaN
        df['amount_numeric'] = pd.to_numeric(df['amount'], errors='coerce')
        if (df['amount_numeric'] <= 0).any():
            issues_found.append("Non-positive 'amount' found (value <= 0).")
            print("  Issue: Non-positive 'amount' detected.")
        if df['amount_numeric'].isnull().any() and df['amount'].dtype == 'object':
            issues_found.append("Non-numerical 'amount' values detected.")
            print("  Issue: Non-numerical 'amount' values detected (e.g., 'lima puluh ribu').")

    # 4. Check for valid Transaction Types
    if 'transaction_type' in df.columns:
        valid_types = ['SEND', 'RECEIVE', 'TOPUP', 'TRANSFER', 'PAYMENT', 'BILL_PAYMENT']
        if not df['transaction_type'].isin(valid_types).all():
            issues_found.append("Invalid 'transaction_type' values found. Expected {', '.join(valid_types)}.")
            print("  Issue: Invalid 'transaction_type' values found.")

    print("--- Valid transactions type check complete ---")

    return issues_found

if __name__ == "__main__":
    raw_data_path = 'data/raw/transactions.csv'
    all_issues = run_data_quality_checks(raw_data_path)

    print("\n --- FINAL DATA QUALITY REPORT ---")
    if all_issues:
        print("\n!!! ISSUES DETECTED !!!")
        for i, issue in enumerate(all_issues):
            print(f"{i+1}. {issue}")
        print(f"\n Total Issues found: {len(all_issues)}")
        print("Please review the raw data and correct the identified issues.")
    else:
        print("\nAll primary data quality checks passed. Data looks good for further processing.!")
    print("--- REPORT END ---")