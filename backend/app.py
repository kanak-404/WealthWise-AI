from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

import pandas as pd

from services.insights import generate_insights
from models.predictors import train_model, predict_overspending
from services.chatbot import generate_response

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return "WealthWise AI Backend Running 🚀"

@app.route('/summary')
def summary():
    df = pd.read_csv('../data/sample_transactions.csv')

    total = df['amount'].sum()
    by_category = df.groupby('category')['amount'].sum().to_dict()

    insights = generate_insights(df)

    # Train model
    model, threshold = train_model(df)

    # Simulate current state
    current_day = 20
    current_spend = 1800
    is_weekend = 0

    prediction = predict_overspending(model, current_day, current_spend, is_weekend)

    score = calculate_health_score(total)

    return jsonify({
        "total_spending": int(total),
        "category_breakdown": by_category,
        "insights": insights,
        "prediction": "Overspending likely ⚠️" if prediction else "Spending under control ✅",
        "prediction_reason": f"Daily spending above average threshold ₹{int(threshold)}",
        "financial_health_score": score
    })
        
@app.route('/chat', methods=['POST'])
def chat():
    df = pd.read_csv('../data/sample_transactions.csv')

    total = df['amount'].sum()

    # Reuse prediction logic
    model, threshold = train_model(df)
    prediction_flag = predict_overspending(model, 20, 1800, 0)

    prediction = "Overspending likely ⚠️" if prediction_flag else "Spending under control ✅"

    context = {
        "total_spending": int(total),
        "prediction": prediction
    }

    user_question = request.json.get("question")

    response = generate_response(user_question, context)

    return jsonify({
        "question": user_question,
        "answer": response
    })

@app.route('/simulate', methods=['POST'])
def simulate():
    df = pd.read_csv('../data/sample_transactions.csv')

    food_spend = df[df['category'] == 'Food']['amount'].sum()

    reduction_percent = 20  # fixed for now
    savings = int(food_spend * reduction_percent / 100)

    return jsonify({
        "message": f"If you reduce food spending by {reduction_percent}%, you can save ₹{savings} per month."
    })

def calculate_health_score(total_spending):
    # Assume monthly budget = 20000 (you can tweak)
    budget = 20000
    score = 100 - (total_spending / budget * 100)
    return max(0, min(100, int(score)))

if __name__ == '__main__':
    app.run(debug=True)