import uuid
from abc import ABC

from src.domain.model.order_items.order_item_schemas import CreateOrderItemDTO, UpdateOrderItemDTO
from src.domain.model.order_items.order_item_model import OrderItem
from src.domain.ports.repositories.order_repository import IOrderRepository


class OrderItemsServiceInterface(ABC):
    def __init__(self, order_repo: IOrderRepository) -> None:
        raise NotImplementedError

    def get_all_from_order(self, order_id: uuid.UUID):
        pass

    def create(self, input_dto: CreateOrderItemDTO) -> OrderItem:
        pass

    def update_quantity(self, input_dto: UpdateOrderItemDTO) -> OrderItem:
        pass

    def remove_single_item_from_order(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        pass

    def remove_all_items_from_order(self, order_id: uuid.UUID) -> None:
        pass
