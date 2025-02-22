import json
import requests
import sys

if len(sys.argv) < 2:
    exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

r = response.json()
# print(json.dumps(response.json(), indent=2))

for result in r["results"]:
    print(result["trackName"])
    print(result["releaseDate"][:10])


