# to run server : uvicorn app.main:app --reload
# to check websockets browser : https://websocketking.com/?utm_source=chatgpt.com
#connect for websocket : ws://127.0.0.1:8000/ws/vehicle

from fastapi import FastAPI

from app.database import Base, engine
from app.routes import vehicle, telemetry, alerts
from app.routes import websocket


app = FastAPI()

Base.metadata.create_all (bind = engine )

app.include_router(vehicle.router)
app.include_router(telemetry.router)
app.include_router(alerts.router)
app.include_router(websocket.router)

@app.get("/")
def home():
    return {
        "message":"Connected Vehicle Monitoring System Running"
    }
