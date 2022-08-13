from pydantic import BaseModel


class UserCreate(BaseModel):
    USERNAME: str
    PASSWORD: str


class ShowUser(BaseModel):
    USERNAME: str

    class Config():
        orm_mode = True

