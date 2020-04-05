import requests

url = "http://localhost:8000/api/airport/YHZ/IKA/distance"

headers = {
    'Authorization': "Basic bmlsb3VmYXI6dHJpcGFkbWlu",
    }

response = requests.request("GET", url, headers=headers)

print(response.text)