import requests


# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# print(avaliacoes.status_code)
# print(avaliacoes.json())
# print(type(avaliacoes.json()))
