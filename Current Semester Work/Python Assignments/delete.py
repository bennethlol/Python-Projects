import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(api_url)
result = response.json()

print("Status Code:", response.status_code)
print("Delete JSON:", result)
