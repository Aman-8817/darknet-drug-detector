# blockchain_analysis.py

# Sample wallet transactions: wallet_id, timestamp, amount
transactions = [
    {"wallet": "W1", "timestamp": "2025-09-01T01:00:00Z", "amount": 0.5},
    {"wallet": "W1", "timestamp": "2025-09-01T02:00:00Z", "amount": 0.6},
    {"wallet": "W1", "timestamp": "2025-09-01T03:00:00Z", "amount": 0.4},  # Suspicious: frequent small deposits
    {"wallet": "W2", "timestamp": "2025-09-01T01:30:00Z", "amount": 5.0},
    {"wallet": "W3", "timestamp": "2025-09-01T04:00:00Z", "amount": 10.0},
]

def detect_suspicious_wallets(transactions, threshold=1.0, freq=3):
    from collections import Counter, defaultdict
    import datetime

    wallet_small_tx_counts = defaultdict(int)

    for tx in transactions:
        if tx["amount"] <= threshold:
            wallet_small_tx_counts[tx["wallet"]] += 1

    suspicious_wallets = [wallet for wallet, count in wallet_small_tx_counts.items() if count >= freq]
    return suspicious_wallets

if __name__ == "__main__":
    suspicious = detect_suspicious_wallets(transactions)
    print(f"Suspicious wallets with frequent small deposits: {suspicious}")
