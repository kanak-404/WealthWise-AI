def predict_credit(model, input_array):
    pred = model.predict(input_array)[0]

    prob = None
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_array)[0][1]

    return pred, prob