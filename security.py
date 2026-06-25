from passlib.context import CryptContext


from jose import (
    jwt,
    JWTError
)


from datetime import (
    datetime,
    timedelta,
    timezone
)


from fastapi import (
    Depends,
    HTTPException,
    status
)


from fastapi.security import OAuth2PasswordBearer


from sqlalchemy.orm import Session


from database import get_db


from model import alchemy_model


pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password:str):

    return pwd_context.hash(
        password
    )
    
    
def verify_password(
        plain_password,
        hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )
    

SECRET_KEY="mysecretkey"


ALGORITHM="HS256"


ACCESS_TOKEN_EXPIRE_MINUTES=30


def create_access_token(
        data:dict
):

    to_encode=data.copy()


    expire=datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )


    to_encode.update(
        {
            "exp":expire
        }
    )


    token=jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return token


oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="auth/login"
)




def get_current_user(

    token:str=Depends(oauth2_scheme),

    db:Session=Depends(get_db)

):


    try:


        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        username=payload.get(
            "sub"
        )


        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )


    except JWTError:


        raise HTTPException(

            status_code=401,

            detail="Invalid token"

        )



    user=db.query(
        alchemy_model.User
    ).filter(

        alchemy_model.User.username==username

    ).first()



    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



    return user




def admin_required(

current_user=Depends(get_current_user)

):


    if current_user.role!="admin":


        raise HTTPException(

            status_code=403,

            detail="Admin only"

        )


    return current_user







def doctor_required(

current_user=Depends(get_current_user)

):


    if current_user.role!="doctor":


        raise HTTPException(

            status_code=403,

            detail="Doctor only"

        )


    return current_user





def patient_required(

current_user=Depends(get_current_user)

):


    if current_user.role!="patient":


        raise HTTPException(

            status_code=403,

            detail="Patient only"

        )


    return current_user