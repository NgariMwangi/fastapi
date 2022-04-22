from typing import List
from urllib import response

from fastapi import Depends, FastAPI,status,Response,HTTPException
from pydantic import BaseModel
from sqlalchemy import false
import schemas,models,hashing
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from routers import blog,user,authentication
app= FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
def get_db():
    db=SessionLocal() 
    try:
        yield db
    finally:
        db.close()

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
# def create_blog(request:schemas.Blog,db:Session=Depends(get_db)): 
#     new_blog=models.Blog(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',response_model=List[schemas.Showblog],tags=["Blogs"])
# def all_blogs(db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs





# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post('/user',status_code=status.HTTP_201_CREATED,response_model=schemas.Show_user,tags=["users"])
# def new_user(request:schemas.User,db:Session=Depends(get_db)):
#     # hashed_password=pwd_context.hash(request.password)
#     new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.Show_user,tags=["users"])
# def get_user(id:int,db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} is not available")
    
#     return user


