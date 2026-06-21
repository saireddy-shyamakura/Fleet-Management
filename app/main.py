from fastapi import FastAPI

from app.api.alert import router as alert_router
from app.api.company import router as company_router
from app.api.driving_history import router as driving_history_router
from app.api.telemetry import router as telemetry_router
from app.api.user import router as user_router
from app.api.vehicle import router as vehicle_router
from app.api.vehicle_settings import router as vehicle_settings_router

app = FastAPI()

app.include_router(company_router)
app.include_router(alert_router)
app.include_router(driving_history_router)
app.include_router(telemetry_router)
app.include_router(user_router)
app.include_router(vehicle_router)
app.include_router(vehicle_settings_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "API is running"}
