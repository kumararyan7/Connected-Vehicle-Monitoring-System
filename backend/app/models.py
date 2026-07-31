from sqlalchemy import Column,Integer,String,Float
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer,primary_key= True,index= True)
    vehicle_id= Column(String, unique=True)
    model = Column(String)

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer,primary_key=True,index= True)
    vehicle_id = Column(String,unique=True)
    battery = Column(Float)
    speed = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(String)
