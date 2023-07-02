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
                "product_id": "00000000-0000-0000-0000-000000000000",
                "product_quantity": 1,
            }
        }


class CreateOrderItemDTO(OrderItemsDTO):
    ...


class UpdateOrderItemDTO(OrderItemsDTO):
    ...


class RemoveOrderItemDTO(BaseModel):
    order_id: uuid.UUID
    product_id: uuid.UUID

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
                "product_id": "00000000-0000-0000-0000-000000000000",
            }
        }


class OrderItemDTOResponse(BaseModel):
    result: OrderItemsDTO


class OrderItemDTOListResponse(BaseModel):
    result: List[OrderItemsDTO]


class OrderDTO(BaseModel):
    order_id: uuid.UUID
    customer_id: uuid.UUID
    order_items: List[OrderItemsDTO]
    creation_date: datetime.datetime
    order_total: Optional[float]
    status: str

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
                "customer_id": "00000000-0000-0000-0000-000000000000",
                "order_items": [
                    {
                        "order_id": "00000000-0000-0000-0000-000000000000",
                        "product_id": "00000000-0000-0000-0000-000000000000",
                        "product_quantity": 1,
                    }
                ],
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
