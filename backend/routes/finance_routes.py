from flask import Blueprint, request, jsonify
from services.budget_service import analyze_budget
from services.scoring_service import calculate_score
from services.feature_builder import build_features, prepare_model_input
from services.prediction_service import predict_credit
from services.recommendation_service import generate_recommendations
from model.model_loader import load_model

finance_bp = Blueprint('finance', __name__)
model = load_model()

@finance_bp.route('/analyze-finance', methods=['POST'])
def analyze_finance():
    data = request.json

    income = data['income']
    transactions = data['transactions']

    budget = analyze_budget(transactions)
    score = calculate_score(income, budget['total_spent'])

    features = build_features(income, budget, score)
    model_input = prepare_model_input(features)

    pred, prob = predict_credit(model, model_input)

    recs = generate_recommendations(features, budget)

    return jsonify({
        "summary": score,
        "prediction": {
            "approved": bool(pred),
            "probability": float(prob) if prob else None
        },
        "recommendations": recs,
        "categories": budget["category_breakdown"]
    })