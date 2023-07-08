import uuid

from fastapi import APIRouter, Depends, status
from kink import di

from src.config.errors import APIErrorMessage, RepositoryError, ResourceNotFound
from src.adapters.services.order_service import OrderService
from src.domain.model.order.order_schemas import (
    CreateOrderDTO, OrderDTOResponse, OrderDTOListResponse, CreateOrderItemDTO, UpdateOrderItemDTO, RemoveOrderItemDTO,
)

router = APIRouter()


@router.get(
    "/orders", tags=["Orders"],
    response_model=OrderDTOListResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_orders(
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    try:
        result = service.get_all()
    except Exception:
        raise RepositoryError.get_operation_failed()

    return {"result": result}


@router.get(
    "/orders/id/{order_id}", tags=["Orders"],
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
    try:
        result = service.get_by_id(order_id)
    except AttributeError:
        raise ResourceNotFound.get_operation_failed(f"No order with id: {order_id}")
    except Exception:
        raise RepositoryError.get_operation_failed()

    return {"result": result}


@router.post(
    "/orders",  tags=["Orders"],
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
    try:
        result = service.create_order(request)
    except Exception:
        raise RepositoryError.save_operation_failed()

    return {"result": result}


@router.post(
    "/orders/{order_id}/items", tags=["Order Items"],
    response_model=OrderDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def add_order_items(
    request: CreateOrderItemDTO,
    order_id: uuid.UUID,
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    try:
        result = service.create_order_item(order_id, request)
    except Exception:
        raise RepositoryError.save_operation_failed()

    return {"result": result}


@router.put(
    "/orders/{order_id}/items",  tags=["Order Items"],
    response_model=OrderDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def change_order_item_quantity(
    order_id: uuid.UUID,
    request: UpdateOrderItemDTO,
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    try:
        result = service.update_quantity(order_id, request)
    except Exception:
        raise RepositoryError.save_operation_failed()

    return {"result": result}


@router.post(
    "/orders/{order_id}/confirmation", tags=["Orders"],
    response_model=OrderDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def confirm_order(
    order_id: uuid.UUID,
    service: OrderService = Depends(lambda: di[OrderService]),
) -> dict:
    try:
        result = service.confirm_order(order_id)
    except Exception:
        raise RepositoryError.save_operation_failed()

    return {"result": result}


@router.delete(
    "/orders/{order_id}", tags=["Orders"],
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_order(
    order_id: uuid.UUID,
    service: OrderService = Depends(lambda: di[OrderService]),
) -> dict:
    try:
        service.remove_order(order_id)
    except Exception:
        raise RepositoryError.save_operation_failed()

    return {"result": "Order removed successfully"}


@router.delete(
    "/orders/{order_id}/items", tags=["Order Items"],
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_order_item(
    request: RemoveOrderItemDTO,
    service: OrderService = Depends(lambda: di[OrderService])
) -> dict:
    try:
        service.remove_order_item(request.order_id, request.product_id)
    except Exception:
        raise RepositoryError.save_operation_failed()

    return {"result": "Order item removed successfully"}
