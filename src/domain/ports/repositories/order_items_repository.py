import uuid
from abc import ABC, abstractmethod
from typing import List

from src.domain.model.order_items.order_item_model import OrderItem


class IOrderItemsRepository(ABC):

    @abstractmethod
    def get_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> OrderItem:
        pass

    @abstractmethod
    def get_all(self, order_id: uuid.UUID) -> List[OrderItem]:
        pass

    @abstractmethod
    def create(self, item_in: OrderItem) -> OrderItem:
        pass

    @abstractmethod
    def update(self, item_in: OrderItem) -> OrderItem:
        pass

    @abstractmethod
    def remove_one(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        pass

    @abstractmethod
    def remove_all(self, order_id: uuid.UUID) -> None:
        pass
