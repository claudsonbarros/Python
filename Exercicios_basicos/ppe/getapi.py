import requests


r = requests.get(url='https://api.chucknorris.io/jokes/random')
print(r.json())


