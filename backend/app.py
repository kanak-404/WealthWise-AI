from flask import Flask, jsonify
import pandas as pd
from services.insights import generate_insights

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

    return jsonify({
        "total_spending": int(total),
        "category_breakdown": by_category,
        "insights": insights
    })

if __name__ == '__main__':
    app.run(debug=True)