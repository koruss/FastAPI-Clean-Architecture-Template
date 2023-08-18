# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim



# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV DOCKER_ADDRESS=172.17.0.2

ENV DOCKER_PORT=15400


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN python -m pip install pydantic[email]

#Move the .env file
COPY test.env .

WORKDIR /src
COPY . /src



# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /src
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:3400", "-k", "uvicorn.workers.UvicornWorker", "src.__main__:app"]

#CMD ["uvicorn", "__main__:app", "--host=0.0.0.0", "--port=80"]
CMD ["python","./__main__.py"]