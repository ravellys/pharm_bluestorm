from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.patients import list_patients
from schemas.patients import ShowPatients
from db.session import get_db

router = APIRouter()


@router.get("", response_model=List[ShowPatients])
def retreive_all_patients(db: Session = Depends(get_db)):
    jobs = list_patients(db=db)
    return jobs
