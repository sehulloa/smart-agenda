from pydantic import BaseModel

class Appointment(BaseModel):
    client_name: str
    service: str
    date: str  # formato YYYY-MM-DD
    time: str  # formato HH:MM
    status: str = "PENDING"
