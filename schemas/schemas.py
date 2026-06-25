from pydantic import BaseModel

class UserCreate(BaseModel):

    username:str

    password:str

    role:str
    
    

class UserResponse(BaseModel):

    id:int

    username:str

    role:str



    class Config:

        from_attributes=True
        
        
class Token(BaseModel):

    access_token:str

    token_type:str
    
    
class DoctorCreate(BaseModel):

    specialization:str

    experience:int

    availability:str
        
        
class DoctorResponse(BaseModel):

    id:int

    specialization:str

    experience:int

    availability:str


    class Config:

        from_attributes=True
        



class AppointmentCreate(BaseModel):

    doctor_id:int

    date:str

    time:str
    
    
    
class AppointmentResponse(BaseModel):

    id:int

    patient_id:int

    doctor_id:int

    date:str

    time:str

    status:str


    class Config:

        from_attributes=True