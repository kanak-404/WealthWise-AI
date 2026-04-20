def generate_recommendations(features, budget):
    recs = []

    if features["savings_rate"] < 20:
        recs.append("Increase savings rate to at least 20%")

    if features["expense_to_income_ratio"] > 0.8:
        recs.append("Reduce monthly expenses")

    for cat in budget["category_breakdown"]:
        if cat["percentage"] > 40:
            recs.append(f"High spending on {cat['category']}")

    return recs