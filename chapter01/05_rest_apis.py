import requests

BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'

username = 'tomeko74'
api_token = '686a79fd01d8fd5d5f82fe3584659b97422228e5'
header = { 'X-Github-Username': '%s' % username, 'Content-Type': 'application/json', 'Authorization': 'token %s' % api_token,
}

url = "/users/%s/gists" % username
r = requests.get('%s%s' % (BASE_URL, url), headers=header)

gists = r.json()

for gist in gists:
    data = list(gist['files'].values())[0]
    print(data['filename'], data['raw_url'], data['language'])



