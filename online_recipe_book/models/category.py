from pydantic import BaseModel

class CategoryBase(BaseModel):
    name:str

class CategoryCreate(CategoryBase):
    pass

class CategoryReponse(BaseModel):
    id:int
    name:str

class Category(CategoryBase):
    id:int