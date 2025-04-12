import requests

url = "http://localhost:8000/predict-image"
file_path = "tortuga.jpg"  

with open(file_path, "rb") as f:
    files = {"file": ("sample.jpg", f, "image/jpeg")}
    response = requests.post(url, files=files)

print(response.json())
