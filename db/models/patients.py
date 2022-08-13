from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Patients(Base):
    UUID = Column(String, primary_key=True, index=True)
    FIRST_NAME = Column(String)
    LAST_NAME = Column(String)
    DATE_OF_BIRTH = Column(Date)
    TRANSACTION = relationship("Transactions", back_populates="PATIENT")

