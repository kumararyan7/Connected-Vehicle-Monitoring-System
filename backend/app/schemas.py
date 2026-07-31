from pydantic import BaseModel


class VehicleCreate(BaseModel):
    vehicle_id: str
    model: str


class VehicleResponse(BaseModel):
    id: int
    vehicle_id: str
    model: str

    class Config:
        from_attributes = True


class TelemetryCreate(BaseModel):
    vehicle_id: str
    battery: float
    speed: float
    latitude: float
    longitude: float
    temperature: float
    status: str


class TelemetryResponse(BaseModel):
    id: int
    vehicle_id: str
    battery: float
    speed: float
    latitude: float
    longitude: float
    temperature: float
    status: str

    class Config:
        from_attributes = True