import pandas as pd

def generate_insights(df):
    insights = []

    # Total spending
    total_spend = df['amount'].sum()

    # Category insights
    category_spend = df.groupby('category')['amount'].sum()

    # 1. High spending category
    top_category = category_spend.idxmax()
    top_amount = category_spend.max()

    insights.append(f"You spend the most on {top_category} (₹{int(top_amount)}).")

    # 2. Food-specific insight
    if 'Food' in category_spend:
        food_spend = category_spend['Food']
        if food_spend > 2000:
            insights.append("Your food expenses are quite high. Try reducing online orders.")

    # 3. Weekend spending
    df['date'] = pd.to_datetime(df['date'])
    weekend_spend = df[df['date'].dt.dayofweek >= 5]['amount'].sum()

    if weekend_spend > 1000:
        insights.append("You tend to spend more on weekends.")

    # 4. Frequent merchant detection
    top_merchant = df['description'].value_counts().idxmax()
    insights.append(f"You frequently spend at {top_merchant}.")

    return insights