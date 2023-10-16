import requests

END_POINT = "http://localhost:9696/predict"
client = {"job": "retired", "duration": 445, "poutcome": "success"}

response = requests.post(url=END_POINT, json=client).json()

print(response)
