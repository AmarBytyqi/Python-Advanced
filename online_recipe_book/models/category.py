from pydantic import BaseModel

class CategoryBase(BaseModel):
    name:str

class CategoryCreate(CategoryBase):
    pass

class CategoryReponse(baseModel):
    id:int
    name:str

class Category(CategoryBase):
    id:int