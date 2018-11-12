import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'tomeko74'
api_token = '686a79fd01d8fd5d5f82fe3584659b97422228e5'
header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}

url = "/gists"
data = {
  "description": "the description for this gist",
  "public": True,
  "files": {
    "file1.txt": {
      "content": "String file contents"
    }
  }
}

r = requests.post('%s%s' % (BASE_URL, url), headers=header, data=json.dumps(data))
print(r.json()['url'])
