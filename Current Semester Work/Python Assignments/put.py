import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"

test = {"id": 1, "title": "New Task", "body": "This is for my assignment."
}

response = requests.put(api_url, json=test)
result = response.json()

print("Status Code:", response.status_code)
print("Put JSON:", result) 

