import uuid
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class CustomerDTO(BaseModel):
    customer_id: uuid.UUID
    cpf: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "customer_id": "00000000-0000-0000-0000-000000000000",
                "cpf": "000.000.000-00",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@email.com",
                "phone": "(11) 99999-9999"
            }
        }


class CreateCustomerDTO(BaseModel):
    cpf: Optional[str]
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


class CustomerDTOResponse(BaseModel):
    result: CustomerDTO


class CustomerDTOListResponse(BaseModel):
    result: List[CustomerDTO]

