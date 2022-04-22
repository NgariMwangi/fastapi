
from sys import prefix
from typing import List

from fastapi import Depends, FastAPI,status,Response,HTTPException,APIRouter
# from .. import schemas, database, models
# from .. models import *
import models, schemas, models, database
from sqlalchemy.orm import Session
import oauth2
from repository import blog
router=APIRouter(tags=["Blogs"],prefix="/blog")

@router.get('',response_model=List[schemas.Showblog])
def all_blogs(db:Session =Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user) ):
   return blog.get_all(db)
@router.post('',status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.get('/{id}', status_code=200,response_model=schemas.Showblog)
def show(id,response:Response,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.get_by_id(db,id)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.delete(db,id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return (request,db,id)

