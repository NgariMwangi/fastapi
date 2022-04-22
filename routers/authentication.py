from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi import Depends, FastAPI,status,Response,HTTPException,APIRouter

import schemas,database,models,auth_token 
from hashing import Hash

router=APIRouter(tags=["Authentication"])

@router.post('/login')
def login( request:OAuth2PasswordRequestForm= Depends(),db:Session=Depends(database.get_db),):
    print(request.username)
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")

    # generate token and return itaccess_token _expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = auth_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}