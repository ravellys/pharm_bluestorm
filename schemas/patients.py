from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class ShowPatients(BaseModel):
    UUID: str
    FIRST_NAME: str
    LAST_NAME: str
    DATE_OF_BIRTH: Optional[date]

    class Config():
        orm_mode = True

