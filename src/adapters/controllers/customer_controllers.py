from fastapi import APIRouter, Depends, status
from kink import di

from src.config.errors import APIErrorMessage
from src.adapters.services.customer_service import CustomerService
from src.domain.model.customer_schemas import (
    ChangeCustomerDTO,
    CreateCustomerDTO,
)

router = APIRouter(tags=["Customers"])


@router.get(
    "/customers",
    # response_model=CustomerDTO,
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
    "/customers/{cpf}",
    # response_model=CustomerDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_customer_by_cpf(
    cpf: str,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.get(cpf)
    return {"result": result}


@router.post(
    "/customers",
    # response_model=CustomerDTO,
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
    "/customers/{cpf}",
    # response_model=CustomerDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def change_customer_data(
    cpf: str,
    request: ChangeCustomerDTO,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    result = service.update(cpf, request)
    return {"result": result}


@router.delete(
    "/customers/{cpf}",
    # response_model=CustomerDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_customer(
    cpf: str,
    service: CustomerService = Depends(lambda: di[CustomerService])
) -> dict:
    service.remove(cpf)
    return {"result": "Customer removed successfully"}

