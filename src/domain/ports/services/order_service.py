import uuid
from abc import ABC

from src.domain.model.order.order_schemas import CreateOrderDTO, CreateOrderItemDTO
from src.domain.model.order.order_model import Order
from src.domain.model.order.order_item_model import OrderItem
from src.domain.ports.repositories.order_repository import IOrderRepository


class OrderServiceInterface(ABC):
    def __init__(self, order_repo: IOrderRepository) -> None:
        raise NotImplementedError

    def get_by_id(self, order_id: uuid.UUID):
        pass

    def get_all(self):
        pass

    def create_order(self, input_dto: CreateOrderDTO) -> Order:
        pass

    def get_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> OrderItem:
        pass

    def add_item(self, order_id: uuid.UUID, input_dto: CreateOrderItemDTO) -> Order:
        pass

    def remove_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> Order:
        pass

    def confirm_order(self, order_id: uuid.UUID) -> Order:
        pass

    def remove_order(self, order_id: uuid.UUID) -> None:
        pass

    def remove_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        pass

