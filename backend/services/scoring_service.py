def calculate_score(income, total_spent):
    savings = income - total_spent
    savings_rate = (savings / income) if income > 0 else 0

    score = 0

    if savings_rate > 0.3:
        score += 30
    elif savings_rate > 0.15:
        score += 20
    else:
        score += 10

    if total_spent < 0.7 * income:
        score += 30
    elif total_spent < 0.9 * income:
        score += 20
    else:
        score += 10

    score += 40 if savings > 0 else 10

    return {
        "score": score,
        "savings": savings,
        "savings_rate": round(savings_rate * 100, 2)
    }