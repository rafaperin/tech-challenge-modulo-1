import uuid
from typing import List, Optional, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapters.repositories.order_items.order_item_orm import Order_Items
from src.config.config import settings
from src.adapters.repositories.order.order_orm import Orders
from src.domain.model.order.order_model import Order, order_factory
from src.domain.model.order_items.order_item_model import OrderItem, order_item_factory
from src.domain.ports.repositories.order_repository import IOrderRepository

connection_uri = settings.db.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    connection_uri
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class PostgresDBOrderRepository(IOrderRepository):

    def __init__(self, model: Orders, items_model: Order_Items):
        self.model = model
        self.items_model = items_model

    def items_to_entity(self, order_items: List[Order_Items]) -> List[OrderItem]:
        items = []
        for item in order_items:
            item = order_item_factory(
                item.order_id,
                item.product_id,
                item.product_quantity,
            )
            items.append(item)
        return items

    def order_to_entity(self, order: Orders, items: List[OrderItem]) -> Order:
        order = order_factory(
            order.order_id,
            order.customer_id,
            items,
            order.creation_date,
            order.order_total,
            order.status,
        )
        return order

    def get_by_id(self, order_id: uuid.UUID) -> Optional[Order]:
        with SessionLocal() as db:
            order_db = db.query(self.model).filter(self.model.order_id == order_id).first()
            items_db = db.query(self.items_model).filter(self.items_model.order_id == order_id).all()
        items = self.items_to_entity(items_db)
        result = self.order_to_entity(order_db, items)
        return result

    def get_all(self) -> List[Order]:
        result = []
        with SessionLocal() as db:
            orders = db.query(self.model).order_by(self.model.creation_date).all()
            if orders:
                for order in orders:
                    items_db = db.query(self.items_model).filter(self.items_model.order_id == order.order_id).all()
                    items = self.items_to_entity(items_db)
                    order_entity = self.order_to_entity(order, items)
                    result.append(order_entity)
        return result

    def create_order(self, obj_in: Order) -> Order:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        obj_in_data.pop("order_items")
        db_obj = self.model(**obj_in_data)

        with SessionLocal() as db:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        new_order = self.order_to_entity(db_obj, list())
        return new_order

    def create_order_item(self, obj_in: Order_Items) -> List[OrderItem]:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.items_model(**obj_in_data)

        with SessionLocal() as db:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        item_list = [db_obj]
        return self.items_to_entity(item_list)

    def update_item(self, obj_in: OrderItem):
        item_in = vars(obj_in)
        with SessionLocal() as db:
            db_obj = db.query(self.items_model)\
                .filter(self.items_model.order_id == obj_in.order_id and
                        self.items_model.product_id == obj_in.product_id).first()
            obj_data = jsonable_encoder(db_obj, by_alias=False)
            for field in obj_data:
                if field in item_in:
                    setattr(db_obj, field, item_in[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

    def update(self, order_id: uuid.UUID, obj_in: Order) -> Order:
        order_in = vars(obj_in)
        with SessionLocal() as db:
            db_obj = db.query(self.model).filter(self.model.order_id == order_id).first()
            obj_data = jsonable_encoder(db_obj, by_alias=False)
            for field in obj_data:
                if field in order_in:
                    setattr(db_obj, field, order_in[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        with SessionLocal() as db:
            items_db = db.query(self.items_model).filter(self.items_model.order_id == order_id).all()

        items = self.items_to_entity(items_db)
        updated_order = self.order_to_entity(db_obj, items)
        return updated_order

    def remove_order(self, order_id: uuid.UUID) -> None:
        with SessionLocal() as db:
            order = db.query(self.model).filter(self.model.order_id == order_id).first()
            db.delete(order)

            items = db.query(self.items_model).filter(self.items_model.order_id == order_id).all()
            for item in items:
                db.delete(item)
            db.commit()

    def remove_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        with SessionLocal() as db:
            item = db.query(self.items_model).filter(self.items_model.order_id == order_id).filter(
                self.items_model.product_id == product_id).first()
            db.delete(item)
            db.commit()

