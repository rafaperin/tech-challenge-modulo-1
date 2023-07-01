import uuid

from fastapi import APIRouter, Depends, status
from kink import di

from src.adapters.services.order_items_service import OrderItemService
from src.config.errors import APIErrorMessage
from src.adapters.services.order_service import OrderService
from src.domain.model.order.order_schemas import (
    CreateOrderDTO, OrderDTOResponse, OrderDTOListResponse,
)
from src.domain.model.order_items.order_item_schemas import OrderItemDTOResponse, CreateOrderItemDTO, \
    RemoveOrderItemDTO, UpdateOrderItemDTO

router = APIRouter(tags=["Orders"])


@router.get(
    "/orders",
    response_model=OrderDTOListResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_orders(
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    result = service.get_all()
    return {"result": result}


@router.get(
    "/orders/id/{order_id}",
    response_model=OrderDTOResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_order_by_id(
    order_id: uuid.UUID,
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    result = service.get_by_id(order_id)
    return {"result": result}


@router.post(
    "/orders",
    response_model=OrderDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def create_order(
    request: CreateOrderDTO,
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    result = service.create(request)
    return {"result": result}


@router.post(
    "/orders/{order_id}/items",
    response_model=OrderItemDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def add_order_items(
    request: CreateOrderItemDTO,
    service: OrderItemService = Depends(lambda: di[OrderItemService])
) -> dict:
    result = service.create(request)
    return {"result": result}


@router.put(
    "/orders/{order_id}/items",
    response_model=OrderItemDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def change_order_item_quantity(
    request: UpdateOrderItemDTO,
    service: OrderItemService = Depends(lambda: di[OrderItemService])
) -> dict:
    result = service.update_quantity(request)
    return {"result": result}


@router.post(
    "/orders/{order_id}/confirmation",
    response_model=OrderDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def confirm_order(
    order_id: uuid.UUID,
    order_service: OrderService = Depends(lambda: di[OrderService]),
    order_item_service: OrderItemService = Depends(lambda: di[OrderItemService])
) -> dict:
    order_items = order_item_service.get_all_from_order(order_id)
    order = order_service.update_order_total(order_id, order_items)
    result = order_service.confirm_order(order.order_id)
    return {"result": result}


@router.delete(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_order(
    order_id: uuid.UUID,
    order_service: OrderService = Depends(lambda: di[OrderService]),
    order_item_service: OrderItemService = Depends(lambda: di[OrderItemService])
) -> dict:
    order_item_service.remove_all_items_from_order(order_id)
    order_service.remove(order_id)
    return {"result": "Order removed successfully"}


@router.delete(
    "/orders/{order_id}/items/",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_order_item(
    request: RemoveOrderItemDTO,
    order_item_service: OrderItemService = Depends(lambda: di[OrderItemService])
) -> dict:
    order_item_service.remove_single_item_from_order(request.order_id, request.product_id)
    return {"result": "Order item removed successfully"}
