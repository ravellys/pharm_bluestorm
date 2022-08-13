from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class ShowTransactions(BaseModel):
    PATIENT_UUID: str
    PATIENT_FIRST_NAME: str
    PATIENT_LAST_NAME: str
    PATIENT_DATE_OF_BIRTH: Optional[date]
    PHARMACY_UUID: str
    PHARMACY_NAME: str
    PHARMACY_CITY: str
    TRANSACTION_UUID: str
    AMOUNT: float
    TIMESTAMP: str

    class Config():
        orm_mode = True
