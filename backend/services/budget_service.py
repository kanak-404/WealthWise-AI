from collections import defaultdict
from utils.categorizer import categorize

def analyze_budget(transactions):
    totals = defaultdict(float)
    total_spent = 0

    for tx in transactions:
        category = categorize(tx['description'])
        amount = float(tx['amount'])

        totals[category] += amount
        total_spent += amount

    breakdown = []
    for cat, amt in totals.items():
        breakdown.append({
            "category": cat,
            "amount": amt,
            "percentage": round((amt / total_spent) * 100, 2) if total_spent else 0
        })

    return {
        "total_spent": total_spent,
        "category_breakdown": breakdown
    }