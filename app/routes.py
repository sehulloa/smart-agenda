from fastapi import APIRouter
from app.models import Appointment
from app.database import supabase

router = APIRouter()

@router.post("/appointments")
def create_appointment(appointment: Appointment):
    data = supabase.table("appointments").insert(appointment.dict()).execute()
    return {"message": "Appointment created", "data": data.data}

@router.get("/appointments")
def list_appointments():
    data = supabase.table("appointments").select("*").execute()
    return data.data
