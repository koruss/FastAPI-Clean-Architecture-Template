from kink import di

from src.User.Application.UserService import UserService
from src.User.Domain.IUserRepository import IUserRepository
from src.User.Infrastructure.LocalUserRepository import LocalUserRepository
from src.User.Infrastructure.MongoUserRepository import MongoUserRepository
from src.configs.MongoDB import get_db_connection
from src.shared.LocalLogger import LocalLogger
import os

from src.shared.ILogger import ILogger


def UserDI()->None:
    #repository = MongoUserRepository( get_db_connection() )
    repository = LocalUserRepository()
    logger = LocalLogger()
    di[ILogger] = logger
    VERBOSE = os.getenv("VERBOSE")
    di[IUserRepository] =repository
    di[UserService] = UserService(repository,logger,VERBOSE )
    