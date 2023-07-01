import datetime
import uuid
from typing import Optional, List

from pydantic import BaseModel


class OrderItemsDTO(BaseModel):
    order_id: uuid.UUID
    product_id: uuid.UUID
    product_quantity: int

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
                "customer_id": "00000000-0000-0000-0000-000000000000",
                "product_quantity": 1,
            }
        }


class CreateOrderItemDTO(OrderItemsDTO):
    ...


class UpdateOrderItemDTO(OrderItemsDTO):
    ...


class OrderDTOResponse(BaseModel):
    result: OrderItemsDTO


class OrderDTOListResponse(BaseModel):
    result: List[OrderItemsDTO]

