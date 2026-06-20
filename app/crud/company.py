from typing import Optional, cast

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, data: CompanyCreate) -> Company:
    company: Company = Company(**data.model_dump())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def get_company(db: Session, company_id: int) -> Company | None:
    return cast(Optional[Company], db.get(Company, company_id))


def get_companies(db: Session) -> list[Company]:
    return list(db.scalars(select(Company)))


def update_company(db: Session, company_id: int, data: CompanyUpdate) -> Company | None:
    company = get_company(db, company_id)
    if not company:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(company, key, value)

    db.commit()
    db.refresh(company)
    return company


def delete_company(db: Session, company_id: int) -> Company | None:
    company = get_company(db, company_id)
    if not company:
        return None

    db.delete(company)
    db.commit()
    return company
