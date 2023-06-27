from typing import Dict, Any

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Customers(Base):
    cpf = Column(String(14), primary_key=True, index=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    email = Column(String(80), nullable=True)
    phone = Column(String(20), nullable=True)
