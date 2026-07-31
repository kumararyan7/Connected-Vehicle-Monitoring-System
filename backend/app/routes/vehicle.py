from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Vehicle

router = APIRouter()

@router.post("/register-vehicle")
def register_vehicle(vehicle_id: str, model: str):
    db = SessionLocal()

    vehicle = Vehicle(vehicle_id=vehicle_id,model = model)

    db.add(vehicle)
    db.commit()
    db.close()

    return {
        "message":f"Vehicle {vehicle_id} registered"
    }

@router.get("/vehicles")
def get_vehicles():
    db = SessionLocal()

    vehicles = db.query(Vehicle).all()

    db.close()

    return{
        "vehicle": [v.vehicle_id for v in vehicles]
    }