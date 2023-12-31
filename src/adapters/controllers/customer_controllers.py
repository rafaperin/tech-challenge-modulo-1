import uuid
from typing import Any

from fastapi import APIRouter, Depends, status
from kink import di

from src.config.errors import APIErrorMessage, RepositoryError, ResourceNotFound
from src.adapters.services.customer_service import CustomerService
from src.domain.model.customer.customer_schemas import (
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
    try:
        result = service.get_all()
    except Exception:
        raise RepositoryError.get_operation_failed()

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
) -> Any:
    try:
        result = service.get_by_cpf(cpf)
    except ResourceNotFound:
        raise ResourceNotFound.get_operation_failed(f"No customer with cpf: {cpf}")
    except Exception:
        raise RepositoryError.get_operation_failed()

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
    try:
        result = service.get_by_id(customer_id)
    except ResourceNotFound:
        raise ResourceNotFound.get_operation_failed(f"No customer with id: {customer_id}")
    except Exception:
        raise RepositoryError.get_operation_failed()

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
    try:
        result = service.create(request)
    except Exception:
        raise RepositoryError.save_operation_failed()

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
    try:
        result = service.update(customer_id, request)
    except Exception:
        raise RepositoryError.save_operation_failed()

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
    try:
        service.remove(customer_id)
    except Exception as e:
        print(e)
        raise RepositoryError.save_operation_failed()

    return {"result": "Customer removed successfully"}

