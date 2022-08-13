from typing import List, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apis.version1.route_login import get_curret_user_from_token
from db.models.users import Users
from db.repository.patients import list_patients
from schemas.patients import ShowPatients
from db.session import get_db

router = APIRouter()


@router.get("", response_model=List[ShowPatients])
def retreive_all_patients(
        db: Session = Depends(get_db)
        , current_user: Users = Depends(get_curret_user_from_token)
):
    return list_patients(db=db)
