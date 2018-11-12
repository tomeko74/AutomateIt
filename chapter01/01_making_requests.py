import requests

# Get HTTP Request
r = requests.get('http://ip.jsontest.com/')
print("Response object:", r)
print("Response Text:", r.text)

# Search a string with Get call
payload = {'q': 'chetan'}
r = requests.get('https://github.com/search', params=payload)
print("Request URL:", r.url)

# Post call with payload data
payload = {'key1': 'value1'}
r = requests.post("http://httpbin.org/post", data=payload)
print("Response text:", r.status_code)
print("Response text:", r.json())
print("Response text:", r.text)
print("Response text:", r.content)
print("Response text:", r.url)

# How to handle exceptions with requests
try:
    r = requests.get("http://www.google.com/")
except requests.exceptions.RequestException as e:
    print("Error Response:", e.message)
