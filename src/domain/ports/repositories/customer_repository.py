import uuid
from abc import ABC, abstractmethod
from typing import List

from src.domain.model.customer.customer_model import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    def get_by_id(self, customer_id: uuid.UUID) -> Customer:
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Customer:
        pass

    @abstractmethod
    def get_all(self) -> List[Customer]:
        pass

    @abstractmethod
    def create(self, customer_in: Customer) -> Customer:
        pass

    @abstractmethod
    def update(self, customer_id: uuid.UUID, customer_in: Customer) -> Customer:
        pass

    @abstractmethod
    def remove(self, customer_id: uuid.UUID) -> None:
        pass
