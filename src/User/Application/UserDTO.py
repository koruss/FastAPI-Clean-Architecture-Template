from pydantic import BaseModel, EmailStr
# With pydantic we can validate the data is correct


class CredentialsDTO(BaseModel):
    email: EmailStr
    password: str
