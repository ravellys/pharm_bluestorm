from sqlalchemy.orm import Session
from db.models.patients import Patients


def list_patients(db: Session):
    jobs = db.query(Patients).all()
    return jobs
