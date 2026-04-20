def safe_divide(a, b):
    if b == 0:
        return 0
    return a / b


def round_currency(value):
    return round(value, 2)


def find_top_category(category_breakdown):
    if not category_breakdown:
        return None

    return max(category_breakdown, key=lambda x: x['percentage'])['category']


def format_inr(amount):
    return f"₹{round(amount, 2)}"