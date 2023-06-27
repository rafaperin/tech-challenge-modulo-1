from sqlalchemy import Column, String, Integer, DECIMAL

from src.adapters.db_base import Base


class Products(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=True)
    description = Column(String(150), nullable=True)
    category = Column(String(30), nullable=True)
    price = Column(DECIMAL(7, 2), nullable=True)
    image_url = Column(String(150), nullable=True)
