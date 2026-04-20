import re
from services.budget_service import analyze_budget
from services.scoring_service import calculate_score
from services.simulation_service import run_simulation

def generate_ai_response(question, income, transactions):
    q = question.lower()

    budget = analyze_budget(transactions)
    score = calculate_score(income, budget['total_spent'])

    # Affordability
    if "afford" in q:
        amount = int(re.search(r'\d+', q).group())
        savings = income - budget['total_spent']

        if savings > amount:
            return f"You can afford it. Remaining savings ₹{savings - amount}"
        else:
            return f"Not advisable. Short by ₹{amount - savings}"

    # Improvement
    elif "improve" in q:
        sim = run_simulation(income, transactions, 2000, 0)
        return f"Reduce expenses → +{round(sim['impact']['prob_change']*100,1)}% approval chance"

    # Why low
    elif "why" in q:
        return f"Low score due to savings rate {score['savings_rate']}%"

    return "Ask about affordability, savings, or improving approval chances."