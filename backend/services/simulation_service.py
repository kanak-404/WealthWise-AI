from services.budget_service import analyze_budget
from services.scoring_service import calculate_score
from services.feature_builder import build_features, prepare_model_input
from services.prediction_service import predict_credit
from model.model_loader import load_model

model = load_model()

def adjust_transactions(transactions, reduction):
    total = sum(tx['amount'] for tx in transactions)
    ratio = reduction / total if total > 0 else 0

    return [
        {"description": tx['description'], "amount": tx['amount'] * (1 - ratio)}
        for tx in transactions
    ]

def run_simulation(income, transactions, reduce_expense, increase_income):
    # BEFORE
    b1 = analyze_budget(transactions)
    s1 = calculate_score(income, b1['total_spent'])
    f1 = build_features(income, b1, s1)
    p1, prob1 = predict_credit(model, prepare_model_input(f1))

    # AFTER
    new_income = income + increase_income
    new_tx = adjust_transactions(transactions, reduce_expense)

    b2 = analyze_budget(new_tx)
    s2 = calculate_score(new_income, b2['total_spent'])
    f2 = build_features(new_income, b2, s2)
    p2, prob2 = predict_credit(model, prepare_model_input(f2))

    return {
        "before": {"score": s1['score'], "prob": float(prob1)},
        "after": {"score": s2['score'], "prob": float(prob2)},
        "impact": {
            "score_change": s2['score'] - s1['score'],
            "prob_change": float(prob2 - prob1)
        }
    }