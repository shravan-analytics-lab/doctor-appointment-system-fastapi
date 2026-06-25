from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)


from sqlalchemy.orm import Session


from database import get_db


from model import alchemy_model


from schemas import schemas


from security import admin_required



router=APIRouter(
    prefix="/admin",
    tags=["Admin"]
)




@router.get(
    "/users",
    response_model=list[schemas.UserResponse]
)


def get_users(


    db:Session=Depends(get_db),


    current_user=Depends(admin_required)

):


    users=db.query(
        alchemy_model.User
    ).all()



    return users



@router.get(
    "/doctors",
    response_model=list[schemas.DoctorResponse]
)








def get_doctors(


    db:Session=Depends(get_db),


    current_user=Depends(admin_required)

):


    doctors=db.query(

        alchemy_model.DoctorProfile

    ).all()



    return doctors







@router.get(
    "/patients",
    response_model=list[schemas.UserResponse]
)



def get_patients(


    db:Session=Depends(get_db),


    current_user=Depends(admin_required)

):



    patients=db.query(

        alchemy_model.User

    ).filter(

        alchemy_model.User.role=="patient"

    ).all()




    return patients









@router.get(
    "/appointments",
    response_model=list[schemas.AppointmentResponse]
)



def all_appointments(


    db:Session=Depends(get_db),


    current_user=Depends(admin_required)

):



    appointments=db.query(

        alchemy_model.Appointment

    ).all()




    return appointments








@router.delete(
    "/users/{id}"
)


def delete_user(


    id:int,


    db:Session=Depends(get_db),


    current_user=Depends(admin_required)

):



    user=db.query(

        alchemy_model.User

    ).filter(

        alchemy_model.User.id==id

    ).first()



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )




    db.delete(user)



    db.commit()



    return {

        "message":"User deleted"

    }