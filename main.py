import sys
import urllib.request
import json

username = sys.argv[1]

url =  f"https://api.github.com/users/{username}/events"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print(data[0])
print(data[0]["type"])
print(data[0]["repo"]["name"])