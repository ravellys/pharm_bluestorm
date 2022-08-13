from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apis.version1.route_login import get_curret_user_from_token
from db.models.users import Users
from db.repository.pharmacies import list_pharmacies
from schemas.pharmacies import ShowPharmacies
from db.session import get_db

router = APIRouter()


@router.get("", response_model=List[ShowPharmacies])
def retreive_all_pharmacies(db: Session = Depends(get_db), current_user: Users = Depends(get_curret_user_from_token)):
    return list_pharmacies(db=db)
