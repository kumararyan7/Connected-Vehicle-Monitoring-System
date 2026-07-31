ALERT_MESSAGES = {
    "LOW_BATTERY": {
        "message": "Battery level is critically low.",
        "severity": "HIGH"
    },
    "OVERSPEED": {
        "message": "Vehicle is exceeding the speed limit.",
        "severity": "HIGH"
    },
    "HIGH_TEMPERATURE": {
        "message": "Engine temperature is too high.",
        "severity": "CRITICAL"
    },
    "GPS_SIGNAL_LOST": {
        "message": "GPS signal is unavailable.",
        "severity": "MEDIUM"
    },
    "VEHICLE_OFFLINE": {
        "message": "Vehicle is currently offline.",
        "severity": "LOW"
    }
}


def generate_alert_details(alerts: list):
    """
    Convert alert codes into detailed alert objects.
    """
    return [
        {
            "code": alert,
            "message": ALERT_MESSAGES[alert]["message"],
            "severity": ALERT_MESSAGES[alert]["severity"]
        }
        for alert in alerts
        if alert in ALERT_MESSAGES
    ]