import uuid
from typing import Any

from fastapi import APIRouter, Depends, status
from kink import di

from src.config.errors import APIErrorMessage
from src.adapters.services.customer_service import CustomerService
from src.domain.model.customer_schemas import (
    ChangeCustomerDTO, CreateCustomerDTO, CustomerDTOResponse, CustomerDTOListResponse,
)

router = APIRouter(tags=["Customers"])


@router.get(
    "/customers",
    response_model=CustomerDTOListResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_customers(
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.get_all()
    return {"result": result}


@router.get(
    "/customers/cpf/{cpf}",
    response_model=CustomerDTOResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_customer_by_cpf(
    cpf: str,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.get_by_cpf(cpf)
    return {"result": result}


@router.get(
    "/customers/id/{customer_id}",
    response_model=CustomerDTOResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_customer_by_id(
    customer_id: uuid.UUID,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.get_by_id(customer_id)
    return {"result": result}


@router.post(
    "/customers",
    response_model=CustomerDTOResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def create_customer(
    request: CreateCustomerDTO,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.create(request)
    return {"result": result}


@router.put(
    "/customers/{customer_id}",
    response_model=CustomerDTOResponse,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def change_customer_data(
    customer_id: uuid.UUID,
    request: ChangeCustomerDTO,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.update(customer_id, request)
    return {"result": result}


@router.delete(
    "/customers/{customer_id}",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_customer(
    customer_id: uuid.UUID,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    service.remove(customer_id)
    return {"result": "Customer removed successfully"}

