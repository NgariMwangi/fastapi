from typing import List,Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode=True


class Show_user(BaseModel):
    name:str
    email:str
    # blog down here is the table relationship
    blog:List[Blog]
    class Config():
        orm_mode=True

    
class Showblog(BaseModel):
    title:str
    body:str
    creator:Show_user
    class Config():
        orm_mode=True
    
class User(BaseModel):
    name:str
    email:str
    password:str
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str
    class Config():
        orm_mode=True

         
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None