from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Pharmacies(Base):
    UUID = Column(String, primary_key=True, index=True)
    NAME = Column(String)
    CITY = Column(String)
    TRANSACTION = relationship("Transactions", back_populates="PHARMACY")
