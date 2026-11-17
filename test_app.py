# Importa o app que queremos testar
from app import app


# Teste: a página "/" deve responder com sucesso (código 200)
def test_pagina_inicial():
    cliente = app.test_client()  # cliente falso para "visitar" o site
    resposta = cliente.get("/")
    assert resposta.status_code == 200
