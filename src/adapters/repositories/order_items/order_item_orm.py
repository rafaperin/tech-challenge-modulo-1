from sqlalchemy import Column, UUID, Integer

from src.adapters.db_base import Base


class Order_Items(Base):
    order_id = Column(UUID, primary_key=True, nullable=False)
    product_id = Column(UUID, primary_key=True, nullable=False)
    product_quantity = Column(Integer, nullable=False)
