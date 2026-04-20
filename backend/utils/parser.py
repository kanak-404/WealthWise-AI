import pandas as pd

def parse_csv(file):
    df = pd.read_csv(file)

    # Ensure required columns exist
    if 'description' not in df.columns or 'amount' not in df.columns:
        raise ValueError("CSV must contain 'description' and 'amount' columns")

    transactions = []

    for _, row in df.iterrows():
        transactions.append({
            "description": str(row['description']),
            "amount": float(row['amount'])
        })

    return transactions