import requests
from rest_framework import status
from django.test import TransactionTestCase


class Testes(TransactionTestCase):
    
    def setUp(self):
        self.headers = {
            'Authorization': "Token a5e7184fa69960d979971be85295771a5ee0f766",
            }
        self.url_base_cursos = "http://localhost:8000/api/v2/cursos/"
        self.url_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"

    def test_get_cursos(self):
        resultado = requests.get(url=self.url_base_cursos, headers=self.headers)
        # print(resultado)
        # print(resultado.json())
        assert resultado.status_code == status.HTTP_200_OK
        assert resultado.json()['count'] == 4

    def test_post_curso(self):
        novo_curso = {
            'titulo': 'Testando Post 01',
            'url': 'http://www.cubanprogramer.com.br/testando_post_01'
        }
        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)
        # print(resultado.status_code)
        # print(resultado.json())
        assert resultado.status_code == status.HTTP_400_BAD_REQUEST

    def test_put_curso(self):
        novo_curso = {
            'titulo': 'Testando Put 01',
            'url': 'http://www.cubanprogramer.com.br/testando_put_01'
        }
        resultado = requests.put(url="http://localhost:8000/api/v2/cursos/4/", headers=self.headers, data=novo_curso)
        # print(resultado.status_code)
        # print(resultado.json())
        assert resultado.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_curso(self):
        resultado = requests.delete(url="http://localhost:8000/api/v2/cursos/7/", headers=self.headers)
        # print(resultado.status_code)
        # print(resultado.json())
        assert resultado.status_code == status.HTTP_403_FORBIDDEN