from typing import Optional

from pydantic import BaseModel, EmailStr


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
                "price": "9,99",
                "image_url": "https://blog.letskuk.com.br/lanches-gourmet"
            }
        }


def create_product_factory(name: str, description: str, category: str, price: str, image_url: str) -> CreateProductDTO:
    return CreateProductDTO(name=name, description=description, category=category, price=price, image_url=image_url)


class ChangeProductDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[EmailStr]
    price: Optional[float]
    image_url: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Lanche 1",
                "description": "Lanche daora",
                "category": "Lanche",
                "price": "9,99",
                "image_url": "https://blog.letskuk.com.br/lanches-gourmet"
            }
        }


def change_product_factory(first_name: str, last_name: str, email: str, phone: str) -> ChangeProductDTO:
    return ChangeProductDTO(first_name=first_name, last_name=last_name, email=email, phone=phone)
