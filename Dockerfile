# Usar uma imagem base com Python 3.10
FROM python:3.10

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y libpq-dev

# Instalar Poetry
RUN pip install poetry==1.1.12

# Copiar os arquivos do projeto
COPY pyproject.toml poetry.lock ./

# Instalar dependências do projeto
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copiar os arquivos do projeto para o container
COPY . .

# Expor a porta da aplicação
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
