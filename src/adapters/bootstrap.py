from kink import di

from src.adapters.services.customer_service import CustomerService
from src.adapters.repositories.customer_orm import Customers
from src.domain.ports.repositories.customer_repository import ICustomerRepository
from src.adapters.repositories.postgres_client_repository import PostgresDBCustomerRepository


def bootstrap_di() -> None:
    repository = PostgresDBCustomerRepository(Customers)

    di[ICustomerRepository] = repository
    di[CustomerService] = CustomerService(repository)
