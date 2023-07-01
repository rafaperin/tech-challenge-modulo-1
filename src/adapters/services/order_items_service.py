import uuid
from typing import List

from kink import inject

from src.domain.model.order_items.order_item_model import OrderItem
from src.domain.model.order_items.order_item_schemas import CreateOrderItemDTO, UpdateOrderItemDTO

from src.domain.model.order_items.order_item_model import OrderItem, order_item_factory
from src.domain.ports.repositories.order_items_repository import IOrderItemsRepository
from src.domain.ports.services.order_item_service import OrderItemsServiceInterface


@inject
class OrderItemService(OrderItemsServiceInterface):
    def __init__(self, order_repo: IOrderItemsRepository) -> None:
        self._order_repo = order_repo

    def get_all_from_order(self, order_id: uuid.UUID):
        result = self._order_repo.get_all(order_id)
        order_items = []
        for obj in result:
            order = order_item_factory(
                obj.order_id,
                obj.product_id,
                obj.product_quantity,
            )
            order_items.append(order)
        return order_items

    def create(self, input_dto: CreateOrderItemDTO) -> OrderItem:
        order = OrderItem.create(input_dto.order_id, input_dto.product_id, input_dto.product_quantity)
        self._order_repo.create(order)
        return order

    def update_quantity(self, input_dto: UpdateOrderItemDTO) -> OrderItem:
        order_item = self._order_repo.get_order_item(input_dto.order_id, input_dto.product_id)
        order_item.change_product_quantity(input_dto.product_quantity)

        updated_order_item = self._order_repo.update(order_item)
        return updated_order_item

    def remove_single_item_from_order(self, order_id: uuid.UUID, product_id: uuid.UUID) -> None:
        self._order_repo.remove(order_id, product_id)

    def remove_all_items_from_order(self, order_id: uuid.UUID) -> None:
        self._order_repo.remove(order_id)
