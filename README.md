<h1 align="center"> Project CAR API </h1>

<p align="center">
<a href="#-prévia">Prévia</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-objetivo">Objetivo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#️-instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-dbeaver--postgresql">Banco de Dados</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-docker">Docker</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-conclusão">Conclusão</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#licença">Licença</a>
</p>



### 📷 Prévia

![image](https://github.com/user-attachments/assets/aab9e6bc-a7d0-4d84-9018-059b059a01e5)



### 🎯 Objetivo

<h5 align="justify">O Projeto Car API, é um desafio cujo objetivo é criar uma aplicação web em Python/Django para gerenciar os endpoints dos carros. A aplicação permite efetua um CRUD (listar, criar, atualizar e excluir), permissões e token com JWT. Além disso, os dados obtidos da API são armazenados e manipulados em um banco de dados PostgreSQL e Docker, implementando operações CRUD completas para os dados armazenados..</h5>


### 🚀 Como executar 

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 
- Django 
- Django REST Framework
- GIT 
- PostgreSQL
- Docker
- Docker Compose


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

Teste Unitário
```python
python manage.py test
```

#### 👨🏻‍🚀 Endpoints

Para realiza as requisições dos endpoints, primeiro poderá criar via requisição do endpoint `register`, ou super usuário no terminal (`python manage.py createsuperuser`) ou criar dentro do Admin, passando _email_ e _password_ para gerar um Token do JWT(valido por um dia e duranção de 60 minutos, depois tem executar novamente para o Refresh e poderá verificar se já expirando com verify), depois utilizer o Bearer com código de access

 - JWT
   - localhost:8000/api/accounts/login

        ```
        {
        "email": "user@example.com",
        "password": "string"
        }
        ```
    - localhost:8000/api/accounts/login
        ```
        {
          "email": "user@example.com",
          "password": "string",
          "first_name": "string",
          "last_name": "string"
        }
        ```

   - localhost:8000/api/v1/refresh
   - localhost:8000/api/v1/token/verify

No Django REST Framework - DRF, na parte de Cars ou Brands não poderá acessar sem Token JWT, exceto no metodo GET na parte `/brands` que não necessita de token. Dessa forma, recomenta usar algum software (Postman) ou aplicação do VScode (Thunder Client), ou até Swagger para realizar as requisições da API, somente o Brands consegue fazer a requisições.

- GET
  - localhost:8000/api/v2/cars/
  - localhost:8000/api/v2/brands/

- POST
  - localhost:8000/api/v2/cars/
  - localhost:8000/api/v2/brands/

- PUT | PACTH
  - localhost:8000/api/v2/cars/3
  - localhost:8000/api/v2/brands/7
  
- DELETE
  - localhost:8000/api/v2/cars/1
  - localhost:8000/api/v2/brands/6

No Swagger, poderá colocar somente o _access_ no Authorize que gerado por JWT, sem necessita passar Bearer, `Bearer <numero do token do acesso>`.

- Swagger e Redoc:
  - localhost:8000/api/swagger
  - localhost:8000/api/redoc


#### 🦫 Dbeaver | PostgreSQL

Para visualizar as as tabelas no banco de dados, poderá usar o `DBeaver Communty`, com as seguintes configurações: 

- Host: localhost
- Port: 5432
- Banco de dados: car
- Nome de usuário: dev
- Senha: Dev1234@


#### 🐋 DOCKER


Antes de tudo, construa e execute o contêiner Docker:


```bash
docker compose up --build
```

Carregando as `migrates` e `runserver`, acesse:

Após iniciar o contêiner, aplique as migrações no banco de dados PostgreSQL:
```bash
docker compose exec app python manage.py migrate
```

**Acesso ao Site e Painel Administrativo**

Para acessar no site e no painel administrativo, crie um superusuário com o seguinte comando:
```bash
docker compose exec app python manage.py createsuperuser
```
```bash
docker compose exec app python manage.py runserver
```

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

<h5 align="justify">O Projeto Car API integra uma aplicação Django REST Framework com uma API externa, realizando operações CRUD em brands e Cars, assim, e armazenando dados em um banco de dados PostgreSQL. </h5>


## Licença
[MIT License](LICENSE)
