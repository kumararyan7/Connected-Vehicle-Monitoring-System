from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

from app.utils.simulator import generate_vehicle_data
from app.services.monitoring_service import (
    evaluate_vehicle,
    get_vehicle_health
)
from app.services.alert_service import generate_alert_details

router = APIRouter(tags=["WebSocket"])


@router.websocket("/ws/vehicle")
async def vehicle_stream(websocket: WebSocket):
    await websocket.accept()

    print("✅ Client Connected")

    try:
        while True:
            # Generate simulated telemetry
            data = generate_vehicle_data()

            # Evaluate vehicle
            alert_codes = evaluate_vehicle(data)
            health = get_vehicle_health(data)

            # Generate detailed alerts
            alert_details = generate_alert_details(alert_codes)

            # Add monitoring information
            data["health"] = health
            data["alerts"] = alert_details

            # Send data to client
            await websocket.send_json(data)

            # Stream every 2 seconds
            await asyncio.sleep(2)

    except WebSocketDisconnect:
        print("❌ Client Disconnected")

    except Exception as e:
        print(f"⚠ WebSocket Error: {e}")

    finally:
        print("🔌 WebSocket Connection Closed")