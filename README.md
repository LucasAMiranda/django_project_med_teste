🚀 Configuração do Ambiente

![image](https://github.com/user-attachments/assets/4c0cc55f-1c71-456f-8c3e-529c84d9a9d1)
![image](https://github.com/user-attachments/assets/f255fd7a-e313-4373-b875-01c62755d645)
![image](https://github.com/user-attachments/assets/4092c711-cbee-46b8-a7cf-8c3ee90aa61c)
![image](https://github.com/user-attachments/assets/28be7f4d-026e-4e9f-ac8c-fc6c7c4815e5)
![image](https://github.com/user-attachments/assets/8cea1fa3-b360-46a7-8ae4-c6fc7708d63e)
![image](https://github.com/user-attachments/assets/6717486d-9923-40e8-8a5a-1302e959dae9)



1️⃣ Clonar o repositório

git clone https://github.com/LucasAMiranda/django_project_med_teste.git |
cd django_project_med 

2️⃣ Configurar o ambiente virtual com Poetry**
curl -sSL https://install.python-poetry.org | python3 -
Linux: sudo apt install poetry
outros: pip install poetry (precisa ter o python instalado no seu pc)
**obs**: Se já tiver instalado o poetry só rodar o comando no terminal ou CMD: "poetry install" para instalar as dependências do projeto.

3️⃣ Criar o banco de dados e definir variáveis de ambiente**
Crie um arquivo .env na raiz do projeto e adicione:
POSTGRES_DB=django_db

POSTGRES_USER=django_user

POSTGRES_PASSWORD=django_password

4️⃣ Subir os containers Docker
Para iniciar o banco de dados PostgreSQL:
docker-compose up -d

## **Rodar o Projeto**
1️⃣ Aplicar as migrações do banco de dados
poetry run python manage.py migrate

2️⃣ Criar um superusuário para acessar o Django Admin
poetry run python manage.py createsuperuser

3️⃣ Rodar o servidor
poetry run python manage.py runserver

4️⃣ Rodar os Testes
poetry run python manage.py test
Se tudo estiver correto, a saída será algo assim:

Creating test database...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 1 test in 0.567s

OK
Destroying test database...


O projeto estará acessível em:
🔗 http://127.0.0.1:8000/

A interface do Django Rest Framework pode ser acessada em:
🔗 http://127.0.0.1:8000/api/

## **📜 Endpoints Disponíveis**
🔹 Profissionais de Saúde
Método	Endpoint	Descrição
GET	/api/profissionais/	Lista todos os profissionais
POST	/api/profissionais/	Cadastra um novo profissional
PUT	/api/profissionais/{id}/	Edita um profissional
DELETE	/api/profissionais/{id}/	Remove um profissional

🔹 Consultas Médicas
Método	Endpoint	Descrição
GET	/api/consultas/	Lista todas as consultas
POST	/api/consultas/	Cadastra uma nova consulta
PUT	/api/consultas/{id}/	Edita uma consulta
DELETE	/api/consultas/{id}/	Remove uma consulta

🏗 Arquitetura e Tecnologias Utilizadas
📌 Tecnologias Principais:

    Python 3.10.12 🐍
    Django 5.1.6
    Django Rest Framework
    PostgreSQL 14.15
    Docker & Docker Compose 🐳
    Poetry 1.8.4 (Gerenciador de dependências)

📂 Estrutura do Projeto

/django_project_med
│── /src
│   ├── /profissionalsaude
│   │   ├── migrations/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │── /config
│   │   ├── settings.py
│   │   ├── urls.py
│   ├── manage.py
├── .env
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md


⚡ Dúvidas ou Contribuições?

Fique à vontade para abrir issues ou enviar um pull request! 😊
🔗 Repositório: github.com/LucasAMiranda/django_project_med_teste
✉ Contato: lcmschoolinfotech@gmail.com
