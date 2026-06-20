from fastapi import FastAPI

from app.api.company import router as company_router

app = FastAPI()

app.include_router(company_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "API is running"}
