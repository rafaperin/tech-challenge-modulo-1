import datetime
import uuid
from typing import Optional, List

from pydantic import BaseModel


class OrderDTO(BaseModel):
    order_id: uuid.UUID
    customer_id: uuid.UUID
    creation_date: datetime.datetime
    order_total: Optional[float]
    status: str

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
                "customer_id": "00000000-0000-0000-0000-000000000000",
                "creation_date": "2022-12-27 08:26:49.219717",
                "order_total": 0.0,
                "status": "Pending",
            }
        }


class CreateOrderDTO(BaseModel):
    customer_id: uuid.UUID

    class Config:
        schema_extra = {
            "example": {
                "customer_id": "00000000-0000-0000-0000-000000000000"
            }
        }


class OrderDTOResponse(BaseModel):
    result: OrderDTO


class OrderDTOListResponse(BaseModel):
    result: List[OrderDTO]

