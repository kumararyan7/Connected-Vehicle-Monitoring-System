# 🚗 Connected Vehicle Monitoring System

A real-time Connected Vehicle Monitoring System built using **FastAPI**, **SQLite**, **SQLAlchemy**, and **WebSockets**. This backend simulates vehicle telemetry, monitors vehicle health, generates alerts, and streams live vehicle data.

---

## 📌 Features

- 🚘 Vehicle Registration
- 📡 Real-Time Telemetry Collection
- ⚡ Live Vehicle Monitoring using WebSockets
- 🔋 Battery Monitoring
- 🚦 Overspeed Detection
- 🌡️ High Temperature Detection
- 📍 GPS Validation
- 🚨 Alert Generation with Severity Levels
- ❤️ Vehicle Health Evaluation
- 🗄️ SQLite Database Integration
- 📖 Interactive Swagger API Documentation

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **Real-Time Communication:** WebSocket
- **Language:** Python 3.x

---

## 📂 Project Structure

```
backend/
│
├── app/
│   ├── routes/
│   │   ├── vehicle.py
│   │   ├── telemetry.py
│   │   ├── alerts.py
│   │   └── websocket.py
│   │
│   ├── services/
│   │   ├── monitoring_service.py
│   │   ├── alert_service.py
│   │   └── telemetry_service.py
│   │
│   ├── utils/
│   │   └── simulator.py
│   │
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/Connected_Vehicle_Monitoring_System.git

cd Connected_Vehicle_Monitoring_System/backend
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Application runs on

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📡 WebSocket Endpoint

Connect using any WebSocket client:

```
ws://127.0.0.1:8000/ws/vehicle
```

The server streams simulated vehicle telemetry every **2 seconds**.

Example Response

```json
{
    "vehicle_id": "VH001",
    "battery": 82.5,
    "speed": 74.8,
    "temperature": 42.3,
    "latitude": 18.542381,
    "longitude": 73.854762,
    "status": "ACTIVE",
    "health": "HEALTHY",
    "alerts": []
}
```

---

## 📌 Available APIs

### Vehicle APIs

| Method | Endpoint | Description |
|----------|-------------------------|--------------------------|
| POST | `/register-vehicle` | Register a new vehicle |
| GET | `/vehicles` | Get all registered vehicles |

---

### Telemetry APIs

| Method | Endpoint | Description |
|----------|----------------------------|-----------------------|
| POST | `/send-telemetry` | Send telemetry data |
| GET | `/telemetry/{vehicle_id}` | Retrieve telemetry |

---

### Alert API

| Method | Endpoint | Description |
|----------|---------------------|--------------------------|
| POST | `/analyze-vehicle` | Analyze telemetry and generate alerts |

---

## 🚨 Supported Alerts

- LOW_BATTERY
- OVERSPEED
- HIGH_TEMPERATURE
- GPS_SIGNAL_LOST
- VEHICLE_OFFLINE

---

## ❤️ Vehicle Health Status

The monitoring service categorizes vehicle health as:

- HEALTHY
- WARNING
- CRITICAL

---

## 📈 Future Enhancements

- Vehicle CRUD Operations
- User Authentication & Authorization
- Multiple Vehicle Simulation
- Alert History Storage
- Telemetry History Dashboard
- React Frontend
- Interactive Maps Integration
- Fleet Management Dashboard
- Charts & Analytics
- Docker Support
- CI/CD Pipeline
- Unit & Integration Testing

---

## 👨‍💻 Author

**Kumar Aryan**

Software Developer | Automotive Software | FastAPI | Python | Connected Vehicle Systems

---

## 📜 License

This project is created for learning, demonstration, and portfolio purposes.
