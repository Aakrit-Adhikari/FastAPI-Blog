from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from ..db import get_db
from ..Schemas import *
from ..models import *
from ..utils import *
from ..oauth2 import *
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router=APIRouter(
    tags=['Authentication']
)

@router.post('/login',response_model=Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):

    # user credentails only return username and password so use username  below instead of email
    user=db.query(User).filter(User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials.")
    if not verify_password(user_credentials.password,str(user.password)):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invlaid credentials")
    
    # create a token
    access_token=create_access_token(data={"user_id":user.id})
    # return a token
    return {"access_token":access_token,"token_type":"bearer_token"}
