from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base



class User(Base):

    __tablename__="users"


    id=Column(
        Integer,
        primary_key=True,
        index=True
    )


    username=Column(
        String(50),
        unique=True,
        index=True
    )


    password=Column(
        String(255)
    )


    role=Column(
        String(20)
    )
    
    
class DoctorProfile(Base):

    __tablename__="doctor_profiles"



    id=Column(
        Integer,
        primary_key=True
    )


    user_id=Column(
        Integer,
        ForeignKey("users.id")
    )


    specialization=Column(
        String(100)
    )


    experience=Column(
        Integer
    )


    availability=Column(
        String(100)
    )


    user=relationship(
        "User"
    )
    
    
class Appointment(Base):

    __tablename__="appointments"



    id=Column(
        Integer,
        primary_key=True
    )


    patient_id=Column(
        Integer,
        ForeignKey("users.id")
    )


    doctor_id=Column(
        Integer,
        ForeignKey("doctor_profiles.id")
    )


    date=Column(
        String(50)
    )


    time=Column(
        String(50)
    )


    status=Column(
        String(20),
        default="pending"
    )



    patient=relationship(
        "User"
    )


    doctor=relationship(
        "DoctorProfile"
    )