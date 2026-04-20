import numpy as np

def build_features(income, budget, score):
    return {
        "income": income,
        "total_spent": budget['total_spent'],
        "savings": score['savings'],
        "savings_rate": score['savings_rate'],
        "expense_to_income_ratio": budget['total_spent'] / income if income > 0 else 0
    }

def prepare_model_input(f):
    return np.array([[
        f["income"],
        f["total_spent"],
        f["savings"],
        f["savings_rate"],
        f["expense_to_income_ratio"]
    ]])