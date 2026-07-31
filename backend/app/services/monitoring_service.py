from typing import List

LOW_BATTERY_THRESHOLD = 20
HIGH_TEMPERATURE_THRESHOLD = 85
OVERSPEED_THRESHOLD = 120


def evaluate_vehicle(data: dict) -> List[str]:
    alerts = []

    if data.get("battery", 100) < LOW_BATTERY_THRESHOLD:
        alerts.append("LOW_BATTERY")

    if data.get("speed", 0) > OVERSPEED_THRESHOLD:
        alerts.append("OVERSPEED")

    if data.get("temperature", 25) > HIGH_TEMPERATURE_THRESHOLD:
        alerts.append("HIGH_TEMPERATURE")

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if latitude is None or longitude is None:
        alerts.append("GPS_SIGNAL_LOST")

    if data.get("status", "").upper() == "OFFLINE":
        alerts.append("VEHICLE_OFFLINE")

    return alerts


def get_vehicle_health(data: dict) -> str:
    alerts = evaluate_vehicle(data)

    if len(alerts) == 0:
        return "HEALTHY"

    elif len(alerts) == 1:
        return "WARNING"

    else:
        return "CRITICAL"