import requests

r = requests.get(url='https://api.chucknorris.io/jokes/random')
j = r.json()
print(j['value'])


