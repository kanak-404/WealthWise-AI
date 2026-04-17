def generate_response(question, context):
    
    # Simple rule-based system (Phase 1 version)
    if "afford" in question.lower() or "buy" in question.lower():
        if context['prediction'] == "Overspending likely ⚠️":
            return "This purchase may not be safe. You are likely to overspend this month."
        else:
            return "This purchase seems affordable based on your current spending."

    elif "save" in question.lower():
        return "Try reducing food and shopping expenses. These are your top spending areas."

    elif "spend" in question.lower():
        return f"You have spent ₹{context['total_spending']} so far."

    else:
        return "I can help you manage your finances better. Try asking about spending or saving."