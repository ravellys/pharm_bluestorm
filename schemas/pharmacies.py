from pydantic import BaseModel


class ShowPharmacies(BaseModel):
    UUID: str
    NAME: str
    CITY: str

    class Config():
        orm_mode = True
