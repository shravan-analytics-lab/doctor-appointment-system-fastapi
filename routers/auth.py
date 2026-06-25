from fastapi import APIRouter

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)


from sqlalchemy.orm import Session


from fastapi.security import OAuth2PasswordRequestForm


from database import get_db


from model import alchemy_model


from schemas import schemas


from security import (
    hash_password,
    verify_password,
    create_access_token
)





router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED
)


def register(

    request:schemas.UserCreate,

    db:Session=Depends(get_db)

):


    user=db.query(
        alchemy_model.User
    ).filter(

        alchemy_model.User.username==request.username

    ).first()



    if user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )



    new_user=alchemy_model.User(

        username=request.username,


        password=hash_password(
            request.password
        ),


        role=request.role

    )



    db.add(new_user)


    db.commit()


    db.refresh(new_user)



    return new_user








@router.post(
    "/login",
    response_model=schemas.Token
)


def login(

    request:OAuth2PasswordRequestForm=Depends(),

    db:Session=Depends(get_db)

):


    user=db.query(

        alchemy_model.User

    ).filter(

        alchemy_model.User.username==request.username

    ).first()



    if not user:


        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"

        )




    if not verify_password(

        request.password,

        user.password

    ):


        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"

        )





    token=create_access_token(

        {

            "sub":user.username

        }

    )



    return {

        "access_token":token,

        "token_type":"bearer"

    }