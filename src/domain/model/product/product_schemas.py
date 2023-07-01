import uuid
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class ProductDTO(BaseModel):
    product_id: uuid.UUID
    name: str
    description: Optional[str]
    category: str
    price: float
    image_url: str

    class Config:
        schema_extra = {
            "example": {
                "product_id": "00000000-0000-0000-0000-000000000000",
                "name": "Lanche 1",
                "description": "Lanche daora",
                "category": "Lanche",
                "price": "9.99",
                "image_url": "https://blog.letskuk.com.br/lanches-gourmet"
            }
        }


class CreateProductDTO(BaseModel):
    name: str
    description: Optional[str]
    category: str
    price: float
    image_url: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Lanche 1",
                "description": "Lanche daora",
                "category": "Lanche",
                "price": "9.99",
                "image_url": "https://blog.letskuk.com.br/lanches-gourmet"
            }
        }


class ChangeProductDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    price: Optional[float]
    image_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Lanche 1",
                "description": "Lanche daora",
                "category": "Lanche",
                "price": "9.99",
                "image_url": "https://blog.letskuk.com.br/lanches-gourmet"
            }
        }


class ProductDTOResponse(BaseModel):
    result: ProductDTO


class ProductDTOListResponse(BaseModel):
    result: List[ProductDTO]
