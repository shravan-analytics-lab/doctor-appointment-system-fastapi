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


from security import patient_required



router=APIRouter(
    prefix="/patient",
    tags=["Patient"]
)



@router.get(
    "/doctors",
    response_model=list[schemas.DoctorResponse]
)


def view_doctors(

    db:Session=Depends(get_db)

):


    doctors=db.query(

        alchemy_model.DoctorProfile

    ).all()



    return doctors



@router.get(
    "/search",
    response_model=list[schemas.DoctorResponse]
)



def search_doctors(

    specialization:str,


    db:Session=Depends(get_db)

):



    doctors=db.query(

        alchemy_model.DoctorProfile

    ).filter(


        alchemy_model.DoctorProfile.specialization.contains(
            specialization
        )

    ).all()



    return doctors



@router.post(
    "/appointments",
    response_model=schemas.AppointmentResponse,
    status_code=status.HTTP_201_CREATED
)



def book_appointment(


    request:schemas.AppointmentCreate,


    db:Session=Depends(get_db),



    current_user=Depends(patient_required)

):



    doctor=db.query(

        alchemy_model.DoctorProfile

    ).filter(


        alchemy_model.DoctorProfile.id
        ==
        request.doctor_id


    ).first()




    if not doctor:


        raise HTTPException(

            status_code=404,

            detail="Doctor not found"

        )




    appointment=alchemy_model.Appointment(



        patient_id=current_user.id,


        doctor_id=request.doctor_id,


        date=request.date,


        time=request.time,


        status="pending"

    )





    db.add(appointment)


    db.commit()


    db.refresh(appointment)



    return appointment



@router.get(
    "/appointments",
    response_model=list[schemas.AppointmentResponse]
)



def my_appointments(



    db:Session=Depends(get_db),



    current_user=Depends(patient_required)

):



    appointments=db.query(

        alchemy_model.Appointment

    ).filter(


        alchemy_model.Appointment.patient_id
        ==
        current_user.id


    ).all()



    return appointments




@router.delete(
    "/appointments/{id}"
)







def cancel_appointment(


    id:int,


    db:Session=Depends(get_db),



    current_user=Depends(patient_required)

):


    appointment=db.query(

        alchemy_model.Appointment

    ).filter(


        alchemy_model.Appointment.id==id,


        alchemy_model.Appointment.patient_id
        ==
        current_user.id


    ).first()




    if not appointment:


        raise HTTPException(

            status_code=404,

            detail="Appointment not found"

        )





    db.delete(appointment)



    db.commit()




    return {

        "message":"Appointment cancelled"

    }
    
    
    
    
    
    
@router.get(
    "/doctors/search",
    response_model=list[schemas.DoctorResponse]
)


def search_doctor(

    specialization:str,

    db:Session=Depends(get_db)

):


    doctors=db.query(

        alchemy_model.DoctorProfile

    ).filter(

        alchemy_model.DoctorProfile.specialization.contains(
            specialization
        )

    ).all()



    return doctors