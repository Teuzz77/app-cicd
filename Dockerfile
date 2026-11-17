# Usa uma imagem pequena com Python já instalado
FROM python:3.12-slim

# Pasta de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto e instala as dependências
COPY . .
RUN pip install -r requirements.txt

# Comando que roda quando o container inicia
CMD ["python", "app.py"]
