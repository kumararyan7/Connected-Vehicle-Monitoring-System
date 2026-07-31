from fastapi import APIRouter

from app.schemas import TelemetryCreate
from app.services.monitoring_service import (
    evaluate_vehicle,
    get_vehicle_health,
)
from app.services.alert_service import generate_alert_details

router = APIRouter(tags=["Alerts"])


@router.post("/analyze-vehicle")
def analyze_vehicle(telemetry: TelemetryCreate):

    data = telemetry.model_dump()

    alert_codes = evaluate_vehicle(data)
    health = get_vehicle_health(data)
    alerts = generate_alert_details(alert_codes)

    return {
        "vehicle_id": telemetry.vehicle_id,
        "health": health,
        "alerts": alerts,
    }