import requests

link = 'http://127.0.0.1:8000/test'

json = {
	'title': 'ASDSADASIFJDS',
	'content' : 'SHIITHISDFSDSDF',
}

response = requests.post(link, json=json)

print(response, )