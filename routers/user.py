from sys import prefix
from typing import List
from fastapi import Depends, FastAPI,status,Response,HTTPException,APIRouter
# from .. import schemas, database, models
# from .. models import *
import models, schemas, models, database,hashing,oauth2
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from repository import user


router=APIRouter(tags=["Users"],prefix="/user")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



@router.post('',status_code=status.HTTP_201_CREATED,response_model=schemas.Show_user)
def new_user(request:schemas.User,db:Session=Depends(database.get_db)):
    return user.create_user(db,request)


@router.get('/{id}',response_model=schemas.Show_user)
def get_users(id:int,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.get_users(db,id)