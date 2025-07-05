import pandas as pd

def load_transaction_data(file_path):
    """Loads transaction data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} rows from {file_path}")
        print("First 5 rows:")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None

if __name__ == "__main__":
    # Path to transactions data
    raw_data_path = '../data/raw/transactions.csv'

    transactions_df = load_transaction_data(raw_data_path)

    if transactions_df is not None:
        print("\nData loading complete. Ready for quality checks.")