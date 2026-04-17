import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    df['date'] = pd.to_datetime(df['date'])

    # Feature engineering
    df['day'] = df['date'].dt.day
    df['is_weekend'] = df['date'].dt.dayofweek >= 5

    # Aggregate daily spending
    daily = df.groupby('day').agg({
        'amount': 'sum',
        'is_weekend': 'max'
    }).reset_index()

    # Create target (overspending threshold)
    threshold = daily['amount'].mean()

    daily['overspend'] = (daily['amount'] > threshold).astype(int)

    X = daily[['day', 'amount', 'is_weekend']]
    y = daily['overspend']

    model = RandomForestClassifier()
    model.fit(X, y)

    return model, threshold


def predict_overspending(model, current_day, current_spend, is_weekend):
    prediction = model.predict([[current_day, current_spend, is_weekend]])[0]
    return int(prediction)