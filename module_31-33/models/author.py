from pydantic import BaseModel

class AuthorBase(BaseModel):
    name:str

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(BaseModel):
    name:str
    id:int

class Author(AuthorBase):
    id:int