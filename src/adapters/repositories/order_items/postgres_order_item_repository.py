import uuid
from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.adapters.repositories.order_items.order_item_orm import Order_Items
from src.domain.model.order_items.order_item_model import OrderItem, order_item_factory
from src.domain.ports.repositories.order_items_repository import IOrderItemsRepository

connection_uri = settings.db.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    connection_uri
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class PostgresDBOrderItemRepository(IOrderItemsRepository):

    def __init__(self, model: Order_Items):
        self.model = model

    def to_entity(self, order_item: Order_Items) -> OrderItem:
        order_item = order_item_factory(
            order_item.order_id,
            order_item.product_id,
            order_item.product_quantity
        )
        return order_item

    def get_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> OrderItem:
        with SessionLocal() as db:
            result = db.query(self.model)\
                .filter(self.model.order_id == order_id and
                        self.model.product_id == product_id).first()

        order_item = self.to_entity(result)
        return order_item

    def get_all(self, order_id: uuid.UUID) -> List[OrderItem]:
        order_items = []

        with SessionLocal() as db:
            result = db.query(self.model).filter(self.model.order_id == order_id).all()

        for order_item in result:
            order_items.append(self.to_entity(order_item))
        return order_items

    def create(self, obj_in: OrderItem) -> OrderItem:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data)  # type: ignore

        with SessionLocal() as db:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        new_order_item = self.to_entity(db_obj)
        return new_order_item

    def update(self, obj_in: OrderItem) -> OrderItem:
        order_item_in = vars(obj_in)
        with SessionLocal() as db:
            db_obj = db.query(self.model).\
                filter(self.model.order_id == obj_in.order_id and
                       self.model.product_id == obj_in.product_id).first()
            obj_data = jsonable_encoder(db_obj, by_alias=False)
            for field in obj_data:
                if field in order_item_in:
                    setattr(db_obj, field, order_item_in[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        updated_order_item = self.to_entity(db_obj)
        return updated_order_item

    def remove_one(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        with SessionLocal() as db:
            db_obj = db.query(self.model)\
                .filter(self.model.order_id == order_id and
                        self.model.product_id == product_id).first()
            db.delete(db_obj)
            db.commit()

    def remove_all(self, order_id: uuid.UUID) -> None:
        with SessionLocal() as db:
            db_obj_list = db.query(self.model)\
                .filter(self.model.order_id == order_id).all()
            for obj in db_obj_list:
                db.delete(obj)
            db.commit()
