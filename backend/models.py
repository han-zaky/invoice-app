from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Surovina(Base):
    __tablename__ = "suroviny"

    id = Column(Integer, primary_key=True, index=True)
    nazev = Column(String, nullable=False)
    velikost_baleni = Column(Numeric(10, 3), nullable=False)
    minimalni_mnozstvi = Column(Numeric(10, 3), nullable=True)
