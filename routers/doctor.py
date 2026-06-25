from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)


from sqlalchemy.orm import Session


from database import get_db


from model import alchemy_model


from schemas import schemas


from security import doctor_required



router=APIRouter(
    prefix="/doctor",
    tags=["Doctor"]
)

@router.post(
    "/profile",
    response_model=schemas.DoctorResponse,
    status_code=status.HTTP_201_CREATED
)



def create_profile(

    request:schemas.DoctorCreate,


    db:Session=Depends(get_db),


    current_user=Depends(doctor_required)

):


    existing=db.query(
        alchemy_model.DoctorProfile
    ).filter(

        alchemy_model.DoctorProfile.user_id
        ==
        current_user.id

    ).first()



    if existing:


        raise HTTPException(

            status_code=400,

            detail="Profile already exists"

        )





    profile=alchemy_model.DoctorProfile(


        user_id=current_user.id,


        specialization=request.specialization,


        experience=request.experience,


        availability=request.availability

    )




    db.add(profile)


    db.commit()


    db.refresh(profile)



    return profile


@router.put(
    "/profile",
    response_model=schemas.DoctorResponse
)



def update_profile(


    request:schemas.DoctorCreate,


    db:Session=Depends(get_db),


    current_user=Depends(doctor_required)

):


    profile=db.query(

        alchemy_model.DoctorProfile

    ).filter(

        alchemy_model.DoctorProfile.user_id
        ==
        current_user.id

    ).first()




    if not profile:


        raise HTTPException(

            status_code=404,

            detail="Profile not found"

        )




    profile.specialization=request.specialization


    profile.experience=request.experience


    profile.availability=request.availability



    db.commit()


    db.refresh(profile)



    return profile


@router.get(
    "/appointments",
    response_model=list[schemas.AppointmentResponse]
)


def my_appointments(


    db:Session=Depends(get_db),


    current_user=Depends(doctor_required)

):


    doctor=db.query(

        alchemy_model.DoctorProfile

    ).filter(

        alchemy_model.DoctorProfile.user_id
        ==
        current_user.id

    ).first()




    appointments=db.query(

        alchemy_model.Appointment

    ).filter(

        alchemy_model.Appointment.doctor_id
        ==
        doctor.id

    ).all()



    return appointments