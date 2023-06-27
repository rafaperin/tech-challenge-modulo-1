from abc import ABC, abstractmethod
from typing import List

from src.domain.model.customer_model import Customer


class ICustomerRepository(ABC):
    @abstractmethod
    def get(self, cpf: str) -> Customer:
        pass

    @abstractmethod
    def get_all(self) -> List[Customer]:
        pass

    @abstractmethod
    def create(self, customer_in: Customer) -> Customer:
        pass

    @abstractmethod
    def update(self, customer_in: Customer) -> Customer:
        pass

    @abstractmethod
    def remove(self, cpf: str) -> None:
        pass
