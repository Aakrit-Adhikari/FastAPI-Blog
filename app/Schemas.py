from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
  
