from fastapi import APIRouter, Depends, status
from kink import di

from src.config.errors import APIErrorMessage
from src.adapters.services.product_service import ProductService
from src.domain.model.product_schemas import (
    ChangeProductDTO,
    CreateProductDTO,
)

router = APIRouter(tags=["Products"])


@router.get(
    "/products",
    # response_model=ProductDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_products(
    service: ProductService = Depends(lambda: di[ProductService])
) -> dict:
    result = service.get_all()
    return {"result": result}


@router.get(
    "/products/{product_category}",
    # response_model=ProductDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_all_products_by_category(
    product_category: str,
    service: ProductService = Depends(lambda: di[ProductService])
) -> dict:
    result = service.get_all_by_category(product_category)
    return {"result": result}


@router.get(
    "/products/{product_id}",
    # response_model=ProductDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def get_product_by_id(
    product_id: int,
    service: ProductService = Depends(lambda: di[ProductService])
) -> dict:
    result = service.get(product_id)
    return {"result": result}


@router.post(
    "/products",
    # response_model=ProductDTO,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def create_product(
    request: CreateProductDTO,
    service: ProductService = Depends(lambda: di[ProductService])
) -> dict:
    result = service.create(request)
    return {"result": result}


@router.put(
    "/products/{product_id}",
    # response_model=ProductDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def change_product_data(
    product_id: int,
    request: ChangeProductDTO,
    service: ProductService = Depends(lambda: di[ProductService])
) -> dict:
    result = service.update(product_id, request)
    return {"result": result}


@router.delete(
    "/products/{product_id}",
    # response_model=ProductDTO,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": APIErrorMessage},
               404: {"model": APIErrorMessage},
               500: {"model": APIErrorMessage}}
)
async def remove_product(
    product_id: int,
    service: ProductService = Depends(lambda: di[ProductService])
) -> dict:
    service.remove(product_id)
    return {"result": "Product removed successfully"}

