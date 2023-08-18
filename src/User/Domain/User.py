from pydantic.networks import EmailStr


class User:
    '''User domain model'''
    def __init__(
            self, id: str , name: str, email: EmailStr, password: str
    ) -> None:
        self._name = name
        self._email = email
        self._password = password
        self._id = id

    @property
    def name(self) -> str:
        '''Return the name of the user'''
        return self._name

    @property
    def email(self) -> EmailStr:
        '''Return the email of the user
        Returns:
            EmailStr: _description_
        '''
        return self._email

    @property
    def password(self) -> str:
        '''Return the password of the user'''
        return self._password

    @property
    def id(self) -> str:
        '''Return the id of the user'''
        return self._id
    
    # @_id.setter
    # def _id(self, id: str) -> None:
    #     self._id = id

    def login(self, email: EmailStr, password: str) -> bool:
        '''Return True if the credentials are correct, False otherwise'''
        return True if self._email == email and self._password == password else False
