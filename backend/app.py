from flask import Flask, jsonify
import pandas as pd
from services.insights import generate_insights
from models.predictors import train_model, predict_overspending

app = Flask(__name__)

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

    return jsonify({
        "total_spending": int(total),
        "category_breakdown": by_category,
        "insights": insights,
        "prediction": "Overspending likely ⚠️" if prediction else "Spending under control ✅",
        "prediction_reason": f"Daily spending above average threshold ₹{int(threshold)}"
    })

if __name__ == '__main__':
    app.run(debug=True)