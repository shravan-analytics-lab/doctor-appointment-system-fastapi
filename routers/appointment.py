from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)


from sqlalchemy.orm import Session


from database import get_db


from model import alchemy_model


from schemas import schemas


from security import doctor_required



router=APIRouter(
    prefix="/appointment",
    tags=["Appointment"]
)


def get_doctor_profile(
    db,
    current_user
):


    doctor=db.query(
        alchemy_model.DoctorProfile
    ).filter(

        alchemy_model.DoctorProfile.user_id
        ==
        current_user.id

    ).first()



    if not doctor:


        raise HTTPException(
            status_code=404,
            detail="Doctor profile missing"
        )



    return doctor



@router.put(
    "/{id}/accept",
    response_model=schemas.AppointmentResponse
)


def accept_appointment(

    id:int,


    db:Session=Depends(get_db),


    current_user=Depends(doctor_required)

):


    doctor=get_doctor_profile(
        db,
        current_user
    )



    appointment=db.query(

        alchemy_model.Appointment

    ).filter(


        alchemy_model.Appointment.id==id,


        alchemy_model.Appointment.doctor_id
        ==
        doctor.id


    ).first()



    if not appointment:


        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )




    appointment.status="accepted"



    db.commit()


    db.refresh(appointment)



    return appointment








@router.put(
    "/{id}/reject",
    response_model=schemas.AppointmentResponse
)



def reject_appointment(


    id:int,


    db:Session=Depends(get_db),


    current_user=Depends(doctor_required)

):



    doctor=get_doctor_profile(
        db,
        current_user
    )



    appointment=db.query(

        alchemy_model.Appointment

    ).filter(


        alchemy_model.Appointment.id==id,


        alchemy_model.Appointment.doctor_id
        ==
        doctor.id


    ).first()




    if not appointment:


        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )





    appointment.status="rejected"



    db.commit()


    db.refresh(appointment)




    return appointment








@router.put(
    "/{id}/complete",
    response_model=schemas.AppointmentResponse
)



def complete_appointment(

    id:int,


    db:Session=Depends(get_db),


    current_user=Depends(doctor_required)

):



    doctor=get_doctor_profile(
        db,
        current_user
    )




    appointment=db.query(

        alchemy_model.Appointment

    ).filter(


        alchemy_model.Appointment.id==id,


        alchemy_model.Appointment.doctor_id
        ==
        doctor.id


    ).first()




    if not appointment:


        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )





    if appointment.status!="accepted":


        raise HTTPException(
            status_code=400,
            detail="Only accepted appointments can complete"
        )





    appointment.status="completed"



    db.commit()


    db.refresh(appointment)



    return appointment