# pharm_bluestorm
📜 This project aims to create a private REST API for the financial sector of a healthcare company.
With the API, it will be possible to have access to the purchase information of the companys's patients
by the pharmacies.

#### Endpoints
- /v1/patients [GET]: Endpoint where patient information is listed;
- /v1/pharmacies [GET]: Endpoint where pharmacies information is listed;
- /v1/transactions [GET]: Endpoint where transaction information is listed;
- /v1/users [POST]: Endpoint where users are created;
- /v1/login/token [POST]: Endpoint where the JWT access token is created;

#### Tools and Frameworks:
- [FastAPI](https://fastapi.tiangolo.com/): is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints;
- [Pydantic](https://pydantic-docs.helpmanual.io/): is used to data validation and settings management using python type annotations;
- [Sqlalquemy](https://www.sqlalchemy.org/): is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL;
- [JOSE](https://pypi.org/project/jose/):  is a framework intended to provide a method to securely transfer claims (such as authorization information) between parties. The JOSE framework provides a collection of specifications to serve this purpose. A JSON Web Token (JWT) contains claims that can be used to allow a system to apply access control to resources it owns;
- [Pytest](https://docs.pytest.org/en/7.1.x/):  framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries;
- [Sqlite](https://www.sqlite.org/index.html):  is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

## Using the APIs

1. You can access the API via the swagger `http://127.0.0.1:8000/docs`
![docs](./readme_images/docs.png)

2. You need do the login on the Authorize button:
![docs](./readme_images/login-1.png)
![docs](./readme_images/login-2.png)

3. Now you are availabe ro requests the APIs:
![docs](./readme_images/transactions.png)


4. You can also call the APIs by following curls commands:
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/v1/login/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=lucas&password=123&scope=&client_id=&client_secret='
```

```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/patients' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNhcyIsImV4cCI6MTY2MDQyMjE2N30.0lRtWQQu4zg1ldb38rQTxAG_Sj9PEUm2qVGyfqDgq_E'
```
```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/pharmacies' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNhcyIsImV4cCI6MTY2MDQyMjE2N30.0lRtWQQu4zg1ldb38rQTxAG_Sj9PEUm2qVGyfqDgq_E'
```
```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/transactions' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsdWNhcyIsImV4cCI6MTY2MDQyMjE2N30.0lRtWQQu4zg1ldb38rQTxAG_Sj9PEUm2qVGyfqDgq_E'
```

## 💻  Developer settings

### Requirements
Here is the list of requirements that you need to configure on your machine to use this repository:

1. Python 3 (if you are using Linux it is likely already installed. Run the command python3 -V to verify)
2. Pip (the default Python package installer)

### Using this repository
1. Clone the aplication:
    ```shell
    git clone https://github.com/ravellys/pharm_bluestorm.git
    ```
2. Install the necessary libs:
    ```shell
    pip install requirements.txt
    ```
3. run the project:
    ```shell
    python3 main.py
    ```
4. run the testes:
    ```shell
    pytest
    ```
5. importants links:
   - Swagger: `http://127.0.0.1:8000/docs`
   - doc: `http://127.0.0.1:8000/redoc`

## 🗃 release history
* 13/08/2022 Project start


## 📋 Meta

Lucas Ravelllys: [github](https://github.com/ravellys) | [linkedin](https://www.linkedin.com/in/ravellys/) 

Distributed under MIT License. see `LICENSE` for more information.


## 🚀 Contributions

1. _Fork_ the project (<https://github.com/ravellys/pharm_bluestorm/fork>)
2. Create a _branch_ for your modify (`git checkout -b feature/fooBar`)
3. _Commit_ your changes (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Create a new _Pull Request_


