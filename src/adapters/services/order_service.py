import uuid
from typing import List

from kink import inject

from src.domain.model.order_items.order_item_model import OrderItem
from src.domain.model.order.order_schemas import CreateOrderDTO

from src.domain.model.order.order_model import Order, order_factory
from src.domain.ports.repositories.order_repository import IOrderRepository
from src.domain.ports.services.order_service import OrderServiceInterface


@inject
class OrderService(OrderServiceInterface):
    def __init__(self, order_repo: IOrderRepository) -> None:
        self._order_repo = order_repo

    def get_by_id(self, order_id: uuid.UUID):
        result = self._order_repo.get_by_id(order_id)

        order = order_factory(
            result.order_id,
            result.customer_id,
            result.creation_date,
            result.order_total,
            result.status,
        )
        return order

    def get_all(self):
        result = self._order_repo.get_all()
        orders = []
        for obj in result:
            order = order_factory(
                obj.order_id,
                obj.customer_id,
                obj.creation_date,
                obj.order_total,
                obj.status,
            )
            orders.append(order)
        return orders

    def create(self, input_dto: CreateOrderDTO) -> Order:
        order = Order.create_new_order(input_dto.customer_id)
        self._order_repo.create(order)
        return order

    def update_order_total(self, order_id: uuid.UUID, order_items: List[OrderItem]) -> Order:
        order = self._order_repo.get_by_id(order_id)

        new_total = order.calculate_order_total(order_items)
        order.update_order_total(new_total)

        updated_order = self._order_repo.update(order_id, order)
        return updated_order

    def confirm_order(self, order_id: uuid.UUID) -> Order:
        order = self._order_repo.get_by_id(order_id)
        order.confirm_order()
        updated_order = self._order_repo.update(order_id, order)
        return updated_order

    def remove(self, order_id: uuid.UUID) -> None:
        self._order_repo.remove(order_id)
