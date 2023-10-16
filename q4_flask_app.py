import pickle

from flask import Flask, request, jsonify


def load(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


model = load("model1.bin")
dv = load("dv.bin")
app = Flask("credit-card-model")


@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()

    X = dv.transform(client)
    y_pred = model.predict_proba(X)[0, 1]
    bool_get_card = y_pred > 0.55

    result = {"get_card_proba": float(y_pred), "get_card": bool(bool_get_card)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
