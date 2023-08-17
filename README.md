# Ecommerce-Backend

Just a practice project made by **Kenneth Corrales**


To start working on this project for first time its recommended to create a virtual environment to create it, you can use the command

```sh
  $ python -m venv venv
```

Or in linux:
```sh
  $ python3 -m venv .venv
```
Once the virutal environment its created and activated, you can start installing the dependencies using the pip command

```sh
  $ pip install -r requirements.txt

List of dependencies/libraries:
- dotenv python
- fastapi
- uvicorn
- kink
- pydantic


The project is organized to work with the three major parts of hexagonal architecture (Infrastructure,Application and Domain)
to understand more about this 

https://blog.szymonmiks.pl/p/hexagonal-architecture-in-python/

You can run the project by running the __main__.py


To build the docker image and run the container execute the following commands

Create Image:
```sh
  $ docker image build -t backend .
```

Create Container:
```sh
  $ docker container run --publish 8001:15400 --name backend backend --reload
```

With this the project you can call the API in the localhost:8001

*** COMMENTS ********************************

Study "cls" python  used in errors.py