import random 
import time

def generate_vehicle_data():

    return{
        "battery": random.randint(10,100),
        "speed": random.randint(0,150),
        "latitude" : round(random.uniform(18.50,18.60),6),
        "longitude" : round(random.uniform(73.80,73.90),6),
        "status": "ACTIVE"
    }