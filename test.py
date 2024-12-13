# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        conteudo_esperado = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cristiano Feliciano da Silva</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: white;
                    background: linear-gradient(to bottom right, #1e3c72, #2a5298);
                    background-image: url('https://images.unsplash.com/photo-1581091012184-d942c9a73310?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080');
                    background-size: cover;
                    background-position: center;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }
                h1 {
                    font-size: 3em;
                    margin: 0.5em 0;
                }
                p {
                    font-size: 1.5em;
                    margin: 0.2em 0;
                    max-width: 600px;
                }
            </style>
        </head>
        <body>
            <h1>Cloud & DevOps</h1>
            <p>Bem-vindo ao portfólio de Cristiano Feliciano da Silva, especialista em Cloud Computing e DevOps.</p>
            <p>Aprimorando processos, otimizando infraestruturas e entregando soluções robustas e inovadoras.</p>
        </body>
        </html>
        """.strip()
        self.assertEqual(self.result.data.decode('utf-8').strip(), conteudo_esperado)

if __name__ == "__main__":
    unittest.main()
