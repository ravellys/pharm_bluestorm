from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apis.version1.route_login import get_curret_user_from_token
from db.models.users import Users
from db.repository.transactions import list_transactions
from schemas.transactions import ShowTransactions
from db.session import get_db

router = APIRouter()


@router.get("", response_model=List[ShowTransactions])
def retreive_all_transactions(
        db: Session = Depends(get_db)
        , current_user: Users = Depends(get_curret_user_from_token)
        , PATIENT_NAME: str = None
        , PHARMACY_NAME: str = None
        , PHARMACY_CITY: str = None
):
    params = {
        'P.FIRST_NAME || P.LAST_NAME': PATIENT_NAME,
        'PH.NAME': PHARMACY_NAME,
        'PH.CITY': PHARMACY_CITY
    }
    return list_transactions(db=db, **params)
