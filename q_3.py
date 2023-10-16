import pickle


def load(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


model = load("model1.bin")
dv = load("dv.bin")
client = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print(y_pred)
