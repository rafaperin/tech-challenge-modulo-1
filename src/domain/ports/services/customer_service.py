from abc import ABC

from src.domain.model.customer_schemas import CreateCustomerDTO, ChangeCustomerDTO
from src.domain.model.customer_model import Customer
from src.domain.ports.repositories.customer_repository import ICustomerRepository


class CustomerServiceInterface(ABC):
    def __init__(self, customer_repo: ICustomerRepository) -> None:
        raise NotImplementedError

    def get(self, cpf: str):
        pass

    def get_all(self):
        pass

    def create(self, input_dto: CreateCustomerDTO) -> Customer:
        pass

    def update(self, cpf: str, input_dto: ChangeCustomerDTO) -> Customer:
        pass

    def remove(self, cpf: str) -> None:
        pass

