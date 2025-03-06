<h1 align="center"> Project CAR API </h1>

<p align="center">
<a href="#-prévia">Prévia</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-objetivo">Objetivo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#️-instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#️-apis">APIs</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-dbeaver--postgresql">Banco de Dados</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-docker">Docker</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-conclusão">Conclusão</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>



### 📷 Prévia

![Project car](https://github.com/user-attachments/assets/46176c44-651e-4cd9-8ed1-d5b14862c78d)



### 🎯 Objetivo

Este projeto Car API foi desenvolvido como uma forma de aprimorar meus conhecimentos e habilidades em desenvolvimento de software, explorando tecnologias modernas e práticas recomendadas. O objetivo principal foi criar uma API robusta e eficiente, capaz de gerenciar dados de carros e marcas, utilizando Django REST Framework, PostgreSQL e Docker.

Através deste projeto, pude:

* Consolidar meus conhecimentos em desenvolvimento de APIs RESTful com Django REST Framework.
* Aprofundar meu entendimento sobre autenticação e autorização com JWT.
* Explorar o uso de bancos de dados relacionais com PostgreSQL.
* Aprender a containerizar aplicações com Docker e Docker Compose.
* Praticar testes unitários para garantir a qualidade do código.
* Utilizar ferramentas como Postman e Swagger para testar e documentar a API.


### 🚀 Como executar 

#### 💻 Pré-requisitos

Antes de começar, verifique se atendeu aos seguintes requisitos:

- Python 
- Django 
- Django REST Framework
- GIT 
- PostgreSQL
- Docker
- Docker Compose
- Postman(opcional)


#### 🛠️ Instalação


🦑 Faça o clone do projeto:

```
git clone git@github.com:pedro-hnrq/Project-Car-API.git
```  
Após clonar o repositório acesse o diretório
```
cd Project-Car-API
``` 
execute os comandos abaixo para criar arquivo de variáveis de ambiente a partir de exemplos. (Lembre-se de modificá-los)

```
mv env .env
``` 

#### 🎟️ Ambiente Virtual
Criar Virtualização
```python
python -m venv .venv
```

Ativar o projeto.

```python
source .venv/bin/activate
```
Instalar as dependências
```python
pip install -r requirements.txt
```


Na primeira vez é necessário executar esse comando para aplicar as migrações do banco de dados
```python
python manage.py migrate
```

Criando super usuário para acessar o painel administrativo
```python
python manage.py createsuperuser
```

Executando o Projeto
```python
python manage.py runserver
```

🧪 Teste Unitário



Executar o testes unitários da aplicação `accounts`:

```python
python manage.py test accounts
```

Executar o testes unitários da aplicação `cars`:

```python
python manage.py test cars
```

Cobertura de Testes - Coverage

1. Executar os testes com cobertura na aplicação `accounts`:
    ```
    coverage run manage.py test accounts
    ```
2. Executar os testes com cobertura na aplicação `cars`:
    ```
    coverage run manage.py test cars
   ```
3. Gerar o relatório de cobertura:
    ```
    coverage report -m
   ```
4. Gerar o relatório de cobertura em HTML:
    ```
    coverage html
   ```
   

#### 🗺️ APIs

Este guia detalhado irá te mostrar como usar a API de Carros e Marcas, desde a autenticação até a realização de operações com carros e marcas.

🔐 Autenticação - JWT
 
 Antes de começarmos a interagir com a API, precisamos obter um token de acesso JWT (JSON Web Token). Esse token é como uma chave que garante que você tenha permissão para acessar os recursos protegidos da API.

 Existem três maneiras de obter um token:

 1. Criar um usuário: Você pode criar um usuário diretamente pela API. 
 Endpoint: `POST /api/accounts/register`
    ```
      {
        "email": "user@example.com",
        "password": "your_password",
        "first_name": "John",
        "last_name": "Doe"
      }
    ```
    Sucesso da resposta (201 Created)
    ```
      {
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
      }
    ```

 2. Superusuário: Utilize o comando `python manage.py createsuperuser` no terminal para criar um superusuário com acesso total.
 3. Painel Admin: Acesse o painel de administração do Django e crie um usuário por lá.

Após criar o usuário, você pode obter o token JWT usando login, fornecendo o email e a senha do usuário.

Endpoint: `POST /api/accounts/login`
```
{
    "email": "user@example.com",
    "password": "string"
}
```
Sucesso da resposta (200 OK)
```
{
  "access_token": "your_jwt_token",
  "refresh_token": "your_refresh_token",
  "type": "Bearer",
  "expiration_at": 1741130263,
  "issued_at": 1741043863,
  "user": {
    "id": 1,
    "email": "user@example.com"
  }
}
```

_Lembre-se_:

- O token JWT tem validade de um dia e duração de 60 minutos. Após esse período, você precisará renová-lo usando o endpoint `POST /api/accounts/token/refresh/`.
- Você pode verificar se o token expirou usando o endpoint POST `/api/accounts/token/verify/`.

 🚗 Cars Endpoints
 
 | **Método**   | **Endpoint** | **Descrição** |  **Autenticação** |
|------------|-----------|------------------|------------------|
| GET       |  `/api/v2/cars/` | Lista todos os carros    |  SIM  |
|  GET | `/api/v2/cars/:id/`   | Obtenha detalhes individuais do carro   |  SIM |
| POST     | `/api/v2/cars/`   | Criar novo carro |  SIM |
|  PUT | `/api/v2/cars/:id/`   | Atualizar registro completo do carro   | SIM  |
| PATCH     | `/api/v2/cars/:id`   | Atualização parcial | SIM  |
| DELETE     | `/api/v2/cars/:id/`   | Deleta registro do carro | SIM  |

Exemplo de requisição POST:
```
{
  "model": "BMW X2",
  "brand": "BMW",
  "color": "Blue",
  "factory_year": 2023,
  "model_year": 2024,
  "description": "Sports car"
}
```

🏭 Brands Endpoints

| **Método**   | **Endpoint** | **Descrição** |  **Autenticação** |
|------------|-----------|------------------|------------------|
| GET       |  `/api/v2/brands/` | Lista todos os marcas    |  Não  |
|  GET | `/api/v2/brands/:id/`   | Obtenha detalhes individuais da marca   |  Não |
| POST     | `/api/v2/brands/`   | Criar novo marca |  SIM |
|  PUT | `/api/v2/brands/:id/`   | Atualizar registro completo da marca   | SIM  |
| PATCH     | `/api/v2/brands/:id`   | Atualização parcial | SIM  |
| DELETE     | `/api/v2/brands/:id/`   | Deleta registro da marca | SIM  |

Exemplo de requisição POST:
```
{
  "name": "BMW",
  "description": "German automotive manufacturer..."
}
```
🧩 Swagger e Redoc

A API de Carros e Marcas também oferece documentação interativa através do Swagger e do Redoc.

- Swagger: `http://localhost:8000/api/swagger`
- Redoc: `http://localhost:8000/api/redoc`


_Dica_: No Swagger, você pode simplesmente colar o access_token no campo "Authorize" sem precisar adicionar "Bearer" antes.


👨🏻‍🚀 Postman

Importe a Coleção Postman (link para arquivo JSON)

Defina a variável de ambiente:

`BASE_URL_DJANGO = http://localhost:8000`

Estrutura da coleção:
```
Project Car API
├── Auth
│   ├── Login
│   ├── Register
│   ├── Refresh
│   └── Verify
├── Cars
│   ├── List All
│   ├── Get Single
│   ├── Create
│   ├── Update
│   └── Delete
└── Brands
    ├── List All
    ├── Get Single
    ├── Create
    ├── Update
    └── Delete

```



#### 🦫 Dbeaver | PostgreSQL

Para visualizar as as tabelas no banco de dados, poderá usar o `DBeaver Communty`, com as seguintes configurações: 

- Host: localhost
- Port: 5432
- Banco de dados: car
- Nome de usuário: dev
- Senha: Dev1234@


#### 🐋 DOCKER

Para facilitar a execução e o desenvolvimento da API, utilizamos o Docker para criar um ambiente isolado e consistente. Siga os passos abaixo para colocar a API para rodar em um contêiner:

1. Configurando o `.env`:

    Altere a variável `POSTGRES_HOST` de `localhost` para `db`.

2. Iniciando os Contêineres: 

    Navegue até o diretório `Docker` e execute o seguinte comando para construir e iniciar os contêineres:


    ```bash
    docker compose up --build
    ```
3. Aplicando as Migrações:

    Após iniciar os contêineres, execute o seguinte comando para aplicar as migrações do banco de dados PostgreSQL:

    ```bash
    docker compose exec app python manage.py migrate
    ```
4. Criando um Superusuário:
    
    Para acessar o painel administrativo do Django, crie um superusuário com o seguinte comando:
    ```bash
    docker compose exec app python manage.py createsuperuser
    ```

5. Iniciando o Servidor de Desenvolvimento:

    Inicie o servidor de desenvolvimento do Django com o seguinte comando:

    ```bash
    docker compose exec app python manage.py runserver 0.0.0.0:8000
    ```

6. Outros Comandos Úteis:

    Para iniciar novamente:
    ```bash
    docker compose up -d
    ```
    Iniciar somente o Banco de Dados:

    ```bash
    docker compose up -d db
    ```

    Para poder **Parar** a aplicação no docker basta executar
    ```bash
    docker compose down
    ```



#### 📓 Conclusão

O Projeto Car API é uma aplicação Django REST Framework completa e robusta, que oferece funcionalidades de CRUD para carros e marcas, utilizando um banco de dados PostgreSQL para armazenamento persistente.

Para garantir a qualidade e a confiabilidade da API, foram utilizados os seguintes recursos e ferramentas:

- Docker: Para criar um ambiente de desenvolvimento isolado e consistente.
- Postman/Swagger: Para testar e documentar os endpoints da API de forma interativa.
- Testes Unitários: Para garantir que cada componente da API funcione corretamente e para prevenir regressões.

Além disso, a API utiliza autenticação JWT para proteger os endpoints e garantir que apenas usuários autorizados possam acessar os recursos protegidos.

Com este projeto, poderá gerenciar carros e marcas de forma eficiente e segura, seja para uso pessoal ou para integrar em outras aplicações.


## Licença
[MIT License](LICENSE)
