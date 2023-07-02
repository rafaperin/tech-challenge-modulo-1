import uuid
from abc import ABC, abstractmethod
from typing import List

from src.domain.model.order.order_model import Order
from src.domain.model.order_items.order_item_model import OrderItem


class IOrderRepository(ABC):
    @abstractmethod
    def get_by_id(self, order_id: uuid.UUID) -> Order:
        pass

    @abstractmethod
    def get_all(self) -> List[Order]:
        pass

    @abstractmethod
    def create_order(self, order_in: Order) -> Order:
        pass

    @abstractmethod
    def create_order_item(self, item_in: OrderItem) -> Order:
        pass

    @abstractmethod
    def update(self, order_id: uuid.UUID, order_in: Order) -> Order:
        pass

    @abstractmethod
    def update_item(self, obj_in: OrderItem):
        pass

    @abstractmethod
    def remove_order(self, order_id: uuid.UUID) -> None:
        pass

    @abstractmethod
    def remove_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        pass
