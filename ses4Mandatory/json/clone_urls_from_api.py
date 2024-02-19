import json
import requests


response = requests.get("https://api.github.com/orgs/python-elective-kea/repos")
repos = json.loads(response.text)

clone_urls = []

for repo in repos: 
    clone_urls.append(repo['clone_url'])

print(clone_urls)