import sys
import urllib.request
import json

# Check username
if len(sys.argv) < 2:
    print("Usage: python main.py <username>")
    sys.exit()

username = sys.argv[1]

url = f"https://api.github.com/users/{username}/events"

# Fetch data
try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

except Exception:
    print("User not found or API error")
    sys.exit()

# Header
print(f"\nRecent Activity for {username}\n")

# Display activities
for event in data:
    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "PushEvent":
        commits = len(event["payload"].get("commits", []))
        print(f"- Pushed {commits} commits to {repo}")

    elif event_type == "CreateEvent":
        print(f"- Created repository/branch in {repo}")

    elif event_type == "WatchEvent":
        print(f"- Starred {repo}")

    elif event_type == "IssuesEvent":
        print(f"- Opened an issue in {repo}")

    elif event_type == "PullRequestEvent":
        print(f"- Opened a pull request in {repo}")

    else:
        print(f"- {event_type} in {repo}")