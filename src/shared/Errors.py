from pydantic import BaseModel
class DomainException(Exception):
    pass


class ResourceNotFoundException(DomainException):
    pass


class RepositoryError(Exception):# Errors that happen on the Infraestructure layer
    @classmethod
    def get_operation_failed(cls) -> "RepositoryError":
        return cls("An error ocurred while retrieving data from the database")

class APIErrorMessage(BaseModel):# Inheritance from BaseModel just to ensure the dataTpes received in the error are correct
    type: str
    message: str