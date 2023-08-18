import os
from src.User.Application.UserDTO import CredentialsDTO
from src.User.Domain.IUserRepository import IUserRepository
from src.User.Domain.UserErrors import UserNotFoundException
from src.shared import ILogger

class UserService:
    def __init__(
        self,
        user_repo:IUserRepository,
        logger:ILogger,
        verbose:bool
        ) -> None:
        self.user_repo = user_repo
        self.logger = logger
        self.verbose = verbose

    def login(self, imputDTO:CredentialsDTO)->bool:
        try:
            user = self.user_repo.get_user(imputDTO.email) # retrieves the user data
            if self.verbose:
                self.logger.log_info("APP: "+"User found in the database")

        except Exception as error:
            if self.verbose:
                self.logger.log_error("APP: " +"User not found")
            raise error
            
        return user.login(imputDTO.email,imputDTO.password)