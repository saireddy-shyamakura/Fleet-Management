from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.company import (
    create_company,
    get_companies,
    get_company,
    update_company,
)
from app.crud.company import (
    delete_company as crud_delete_company,
)
from app.db import get_db
from app.models import Company
from app.schemas.company import CompanyCreate, CompanyResponse, CompanyUpdate

router = APIRouter(prefix="/companies", tags=["companies"])


@router.post("/", response_model=CompanyResponse)
def create(data: CompanyCreate, db: Session = Depends(get_db)) -> CompanyResponse:
    return create_company(db, data)


@router.get("/", response_model=list[CompanyResponse])
def read_all(db: Session = Depends(get_db)) -> list[Company]:
    return get_companies(db)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company_by_id(
    company_id: int, db: Session = Depends(get_db)
) -> CompanyResponse:
    company = get_company(db, company_id)

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company_by_id(
    company_id: int, data: CompanyUpdate, db: Session = Depends(get_db)
) -> CompanyResponse:
    company = update_company(db, company_id, data)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    company = crud_delete_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Deleted successfully"}
