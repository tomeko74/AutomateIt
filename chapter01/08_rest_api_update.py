import requests
import json

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'tomeko74'
api_token = '686a79fd01d8fd5d5f82fe3584659b97422228e5' # mój token do gista
gist_id = '1f678fd9c7e2d35db00061112cb88883' # id pliku file1.txt

header = {  'X-Github-Username': '%s' % username,
            'Content-Type': 'application/json',
            'Authorization': 'token %s' % api_token,
}

data = {
  "description": "Updating the description for this gist",
  "files": {
    "file1.txt": {
      "content": "Updating file contents.."
    }
  }
}

url = "/gists/%s" % gist_id
r = requests.patch('%s%s' %(BASE_URL, url), headers=header, data=json.dumps(data))
print(r.json())
