# Importa o Flask, que serve para criar o site
from flask import Flask

# Cria o aplicativo
app = Flask(__name__)


# Rota principal: quando alguém acessa "/", mostra a mensagem
@app.route("/")
def inicio():
    return "Olá! Meu app de CI/CD está funcionando!"


# Liga o servidor na porta 5000 (0.0.0.0 permite acesso de fora do container)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
