from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic import EmailStr

class PostBase(BaseModel):
    id:int
    title:str
    content:str
    published:bool=True

    class config:
        orm_mode=True


class PostCreate(BaseModel):
    title:str
    content:str

    class config:
        orm_mode=True
  
class UserCreate(BaseModel):
    email:EmailStr
    password:str

    class config:
        orm_mode=True

class UserOut(BaseModel):
    id:int
    email:str
    created_at:datetime
    class config:
        orm_mode=True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[int]=None
