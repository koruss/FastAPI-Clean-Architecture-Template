from abc import ABC, abstractmethod

from src.User.Domain.User import User


class IUserRepository(ABC):#This Interface will be later overloaded with an implementation of the Infrastructure layer

    @abstractmethod #Decorator
    def get_user(self, email:str)->User: # Retrieves the user based on the email
        pass

