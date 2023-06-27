from abc import ABC, abstractmethod
from typing import List

from src.domain.model.product_model import Product


class IProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Product:
        pass

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_all_by_category(self, category: str) -> List[Product]:
        pass

    @abstractmethod
    def create(self, product_in: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product_in: Product) -> Product:
        pass

    @abstractmethod
    def remove(self, id: int) -> None:
        pass
