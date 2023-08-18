# FAST API Clean Architecture Template

Just a practice project made by **Kenneth Corrales**

The project is organized to work with the three major parts of hexagonal architecture (Infrastructure,Application and Domain)
to understand more about this 

https://blog.szymonmiks.pl/p/hexagonal-architecture-in-python/


To start working on this project for first time its recommended to create a virtual environment, to create it, you can use the following command

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
```


### List of dependencies/libraries:
- dotenv python
- fastapi
- uvicorn
- kink
- pydantic


## How to Run IT

First you will need to create a .env file with at least the following variables : 

- VERBOSE: TRUE/FALSE

This project has an example of repository with MongoDB in case you want to use it you also will have to provide the following:

- MONGODB_USERNAME 
- MONGODB_PASSWORD 
- MONGODB_HOST
- MONGODB_DB_NAME 

### Local
You can run the project by running the **__main\_\_.py**

Or Run the makefile

```
make build-local
```

### Docker

To build the docker image and run the container execute the following commands

Create Image:
```sh
  $ docker image build -t backend .
```

Create Container:
```sh
  $ docker container run --publish 8001:15400 --name backend backend
```

With this the project you can call the API in the localhost:8001 15400 in the docker container

