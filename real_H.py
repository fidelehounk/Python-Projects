import requests
import json
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
print(response) # returns a response class
json_data = response.text
posts = json.loads(json_data)
print(posts)

for post in posts:
    print(post['title'])