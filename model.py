from sqlalchemy import Column, Integer, String, Date
from data_base import Base


class Users(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    username = Column(String(255), index=True, nullable=False)
    email = Column(String(255), index=True, nullable=False)
    password = Column(String(255), index=True, nullable=False)
    register_date = Column(Date, index=True)
