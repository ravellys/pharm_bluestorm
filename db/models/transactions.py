from sqlalchemy import Column, String, Numeric, Date, ForeignKey
from db.base_class import Base
from sqlalchemy.orm import relationship


class Transactions(Base):
    UUID = Column(String, primary_key=True, index=True)
    PATIENT_UUID = Column(String, ForeignKey('PATIENTS.UUID'))
    PHARMACY_UUID = Column(String, ForeignKey('PHARMACIES.UUID'))
    AMOUNT = Column(Numeric)
    TIMESTAMP = Column(Date)
    PATIENT = relationship("Patients", back_populates="TRANSACTION")
    PHARMACY = relationship("Pharmacies", back_populates="TRANSACTION")
