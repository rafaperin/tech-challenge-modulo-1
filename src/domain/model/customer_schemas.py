from typing import Optional

from pydantic import BaseModel, EmailStr


class CreateCustomerDTO(BaseModel):
    cpf: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "cpf": "000.000.000-00",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@email.com",
                "phone": "(11) 99999-9999"
            }
        }


def create_customer_factory(cpf: str, first_name: str, last_name: str, email: str, phone: str) -> CreateCustomerDTO:
    return CreateCustomerDTO(cpf=cpf, first_name=first_name, last_name=last_name, email=email, phone=phone)


class ChangeCustomerDTO(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Test",
                "last_name": "User",
                "email": "test@email.com",
                "phone": "(11) 99999-9999"
            }
        }


def change_customer_factory(first_name: str, last_name: str, email: str, phone: str) -> ChangeCustomerDTO:
    return ChangeCustomerDTO(first_name=first_name, last_name=last_name, email=email, phone=phone)
