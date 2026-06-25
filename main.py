from fastapi import FastAPI

from database import engine

from model import alchemy_model

from routers import auth,doctor,appointment,admin,patient



app=FastAPI()



alchemy_model.Base.metadata.create_all(
    bind=engine
)


@app.get("/")
def home():

    return "Doctor API running"



app.include_router(
    auth.router
)

app.include_router(
    patient.router
)

app.include_router(
    doctor.router
)


app.include_router(
    appointment.router
)


app.include_router(
    admin.router
)

