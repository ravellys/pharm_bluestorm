from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from db.base_class import Base
import uuid


class Users(Base):
    UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    USERNAME = Column(String, unique=True, nullable=False)
    PASSWORD = Column(String, nullable=False)
