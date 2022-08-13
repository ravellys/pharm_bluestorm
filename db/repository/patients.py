from sqlalchemy.orm import Session
from db.models.patients import Patients


def list_patients(db: Session):
    return db.query(Patients).all()
