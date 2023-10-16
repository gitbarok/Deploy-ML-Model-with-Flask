import requests

END_POINT = "http://127.0.0.1:5000/predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url=END_POINT, json=client).json()

print(response)
