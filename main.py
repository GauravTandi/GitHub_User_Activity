import sys
import urllib.request

username = sys.argv[1]

url =  f"https://api.github.com/users/{username}/events"

response = urllib.request.urlopen(url)

data = response.read()

print(data)