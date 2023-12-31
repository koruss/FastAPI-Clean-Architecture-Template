import os
from fastapi import APIRouter, Depends
from kink import di
from fastapi.responses import JSONResponse

from src.User.Application.UserDTO import CredentialsDTO
from src.User.Application.UserService import UserService
from src.User.Domain.UserErrors import UserNotFoundException
from src.shared.ILogger import ILogger

verbose = os.getenv('VERBOSE')
UserRouter = APIRouter(
    prefix="/users",
    tags=["users"]
)# The router is a way to manage the different paths in a most organized way,
# if the server reads a /users request will come directly to this router and check its methods


@UserRouter.get("/")# Call the definition of the user Router and the HTTP method GET
def login():
    '''Dummy function to check the status of the user router

    Returns:
        _type_: a JSON response 
    '''
    return JSONResponse(status_code=200, content ={"username": "test", "password": "test"})

'''A simple router function that calls the UserService 

Args:
    request 
    service (_type_, optional): _description_. Defaults to Depends(lambda:di[UserService]).

Returns:
    JSONResponse: 
    '''
@UserRouter.post("/login")
def login(
    request:CredentialsDTO,
    service:UserService = Depends(lambda:di[UserService]),
    logger:ILogger = Depends(lambda:di[ILogger])
    )-> JSONResponse:
    try:
        return service.login(request)

    except UserNotFoundException as error:
        if verbose:
            logger.log_error("ROUTER: "+ str(error))
        return JSONResponse(status_code=404, content=str(error))

