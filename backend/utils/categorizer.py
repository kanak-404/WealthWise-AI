def categorize(desc):
    d = desc.lower()

    if "zomato" in d or "swiggy" in d:
        return "Food"
    elif "uber" in d or "ola" in d:
        return "Transport"
    elif "amazon" in d or "shopping" in d:
        return "Shopping"
    elif "bill" in d:
        return "Bills"
    return "Others"