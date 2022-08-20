import requests

app_id = '6d480379'
app_key = 'ae61e680a47e6506290af41a2a66d862'

q = input("Type an ingredient name? ")
url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(q, app_id, app_key)

response = requests.get(url)

data = response.json()

print(data['count'])