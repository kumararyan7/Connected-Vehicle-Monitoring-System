from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Telemetry

router = APIRouter()

@router.post("/send-telemetry")
def send_telemetry(
    vehicle_id:str ,
    battery  : float ,
    speed : float ,
    latitude : float,
    longitude: float,
    status : str
):
    db = SessionLocal()
    telemetry = Telemetry(
        vehicle_id= vehicle_id,
        battery= battery,
        speed=speed,
        latitude= latitude,
        longitude= longitude,
        status=status
    )

    db.add(telemetry)
    db.commit()
    db.close()

    return {
        "message": "Telemetry recieved"
    }

@router.get("/telemetry/{vehicle_id}")
def get_telemetry(vehicle_id :str):
    db = SessionLocal()

    data= db.query(Telemetry).filter(
        Telemetry.vehicle_id == vehicle_id
    ).all()

    db.close()

    return {
        "vehicle_id" : vehicle_id,
        "records" : len(data)
    }