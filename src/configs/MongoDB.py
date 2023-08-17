import os

from pymongo import MongoClient


def get_db_connection():# return a connection to the mongodb database
    initialPath = 'mongodb+srv://'
    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")
    host = os.getenv("MONGODB_HOST")
    DATABASE_URL = initialPath + username + ":" + password + "@" + host + "/" + "?retryWrites=true&w=majority"
    client =  MongoClient(DATABASE_URL)
    return client.get_database(os.environ.get("MONGODB_DB_NAME"))