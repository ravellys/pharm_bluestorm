from sqlalchemy.orm import Session
from db.models.pharmacies import Pharmacies


def list_pharmacies(db: Session):
    return db.query(Pharmacies).all()
