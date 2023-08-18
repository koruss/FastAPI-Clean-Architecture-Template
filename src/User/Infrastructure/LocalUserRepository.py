from src.User.Domain.IUserRepository import IUserRepository
from src.User.Domain.User import User

import uuid

from src.User.Domain.UserErrors import UserNotFoundException

dict = {}
dict["dummy@dumber.com"] = User(str(uuid.uuid4()), "Kenneth", "dummy@dumber.com","secretsauce")
dict["dumm@dumber.com"] = User(str(uuid.uuid4()), "Kennet", "dumm@dumber.com","secretsauc")
dict["dum@dumber.com"] = User(str(uuid.uuid4()), "Kenne", "dum@dumber.com","secretsau")
dict["dum@dumber.com"] = User(str(uuid.uuid4()), "Kenn", "dum@dumber.com","secretsa")

class LocalUserRepository(IUserRepository):

    def __init__(self):
         self.users_dict = dict # This is a dictionary of users where the key is the email and the value is the user object


    def get_user(self, email: str) -> User:
        if email in self.users_dict:
            return self.users_dict.get(email)
        else:
            raise UserNotFoundException(f"User with email: {email} was not found")
        

    def add_user(self, user):
        self._users.append(user)