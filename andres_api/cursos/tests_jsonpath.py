import requests
import jsonpath


# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeiro)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)