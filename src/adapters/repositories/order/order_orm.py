from sqlalchemy import Column, UUID, String, func, DateTime, DECIMAL, Integer

from src.adapters.db_base import Base


class Orders(Base):
    order_id = Column(UUID, primary_key=True, index=True)
    customer_id = Column(UUID, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    order_total = Column(DECIMAL(7, 2), nullable=True)
    status = Column(String(30), nullable=False)


class Order_Items(Base):
    order_id = Column(UUID, primary_key=True, nullable=False)
    product_id = Column(UUID, primary_key=True, nullable=False)
    product_quantity = Column(Integer, nullable=False)
