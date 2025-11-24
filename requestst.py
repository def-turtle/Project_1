import requests
responce = requests.post('http://www.bing.com')
print(type(responce))
if responce.status_code == 200:
    print(responce.text)