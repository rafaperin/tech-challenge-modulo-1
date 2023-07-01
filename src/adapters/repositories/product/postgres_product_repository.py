import uuid
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.adapters.repositories.product.product_orm import Products
from src.domain.model.product.product_model import Product, product_factory
from src.domain.ports.repositories.product_repository import IProductRepository

connection_uri = settings.db.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    connection_uri
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class PostgresDBProductRepository(IProductRepository):

    def __init__(self, model: Products):
        self.model = model

    def to_entity(self, product: Products) -> Product:
        product = product_factory(
            product.product_id,
            product.name,
            product.description,
            product.category,
            product.price,
            product.image_url
        )
        return product

    def get_by_id(self, product_id: uuid.UUID) -> Optional[Product]:
        with SessionLocal() as db:
            result = db.query(self.model).filter(self.model.product_id == product_id).first()
        product = self.to_entity(result)
        return product

    def get_all(self) -> List[Product]:
        products = []

        with SessionLocal() as db:
            result = db.query(self.model).all()

        for product in result:
            products.append(self.to_entity(product))
        return products

    def get_all_by_category(self, category: str) -> List[Product]:
        products = []

        with SessionLocal() as db:
            result = db.query(self.model).filter(self.model.category == category).all()

        for product in result:
            products.append(self.to_entity(product))
        return products

    def create(self, obj_in: Product) -> Product:
        obj_in_data = jsonable_encoder(obj_in, by_alias=False)
        db_obj = self.model(**obj_in_data)  # type: ignore

        with SessionLocal() as db:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        new_product = self.to_entity(db_obj)
        return new_product

    def update(self, obj_in: Product) -> Product:
        product_in = vars(obj_in)
        with SessionLocal() as db:
            db_obj = db.query(self.model).filter(self.model.product_id == obj_in.product_id).first()
            obj_data = jsonable_encoder(db_obj, by_alias=False)
            for field in obj_data:
                if field in product_in:
                    setattr(db_obj, field, product_in[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        updated_product = self.to_entity(db_obj)
        return updated_product

    def remove(self, product_id: uuid.UUID) -> None:
        with SessionLocal() as db:
            db_obj = db.query(self.model).filter(self.model.product_id == product_id).first()
            db.delete(db_obj)
            db.commit()
