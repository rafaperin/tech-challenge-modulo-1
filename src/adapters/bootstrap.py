from kink import di

from src.adapters.repositories.postgres_product_repository import PostgresDBProductRepository
from src.adapters.repositories.product_orm import Products
from src.adapters.services.customer_service import CustomerService
from src.adapters.repositories.customer_orm import Customers
from src.adapters.services.product_service import ProductService
from src.domain.ports.repositories.customer_repository import ICustomerRepository
from src.adapters.repositories.postgres_customer_repository import PostgresDBCustomerRepository
from src.domain.ports.repositories.product_repository import IProductRepository


def bootstrap_di() -> None:
    repository = PostgresDBCustomerRepository(Customers)
    di[ICustomerRepository] = repository
    di[CustomerService] = CustomerService(repository)

    repository = PostgresDBProductRepository(Products)
    di[IProductRepository] = repository
    di[ProductService] = ProductService(repository)
