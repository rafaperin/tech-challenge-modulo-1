import uuid

from kink import inject

from src.config.errors import ResourceNotFound
from src.domain.model.order.order_item_model import OrderItem
from src.domain.model.order.order_schemas import CreateOrderDTO, CreateOrderItemDTO, UpdateOrderItemDTO

from src.domain.model.order.order_model import Order, order_factory
from src.domain.ports.repositories.order_repository import IOrderRepository
from src.domain.ports.repositories.product_repository import IProductRepository
from src.domain.ports.services.order_service import OrderServiceInterface
from src.domain.ports.services.product_service import ProductServiceInterface


@inject
class OrderService(OrderServiceInterface, ProductServiceInterface):
    def __init__(self, order_repo: IOrderRepository, product_repo: IProductRepository) -> None:
        self._order_repo = order_repo
        self._product_repo = product_repo

    def get_by_id(self, order_id: uuid.UUID):
        result = self._order_repo.get_by_id(order_id)

        if not result:
            raise ResourceNotFound
        else:
            order = order_factory(
                result.order_id,
                result.customer_id,
                result.order_items,
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
                obj.order_items,
                obj.creation_date,
                obj.order_total,
                obj.status,
            )
            orders.append(order)
        return orders

    def create_order(self, input_dto: CreateOrderDTO) -> Order:
        order = Order.create_new_order(input_dto.customer_id)
        self._order_repo.create_order(order)
        return order

    def update_quantity(self, order_id: uuid.UUID, input_dto: UpdateOrderItemDTO) -> Order:
        order = self._order_repo.get_by_id(order_id)
        item = OrderItem.create(order_id, input_dto.product_id, input_dto.product_quantity)
        product = self._product_repo.get_by_id(input_dto.product_id)

        order.update_item_quantity(item, product.price)

        self._order_repo.update_item(item)
        updated_order = self._order_repo.update(order_id, order)
        return updated_order

    def create_order_item(self, order_id: uuid.UUID, input_dto: CreateOrderItemDTO) -> Order:
        item = self._order_repo.get_order_item(order_id, input_dto.product_id)
        if item:
            update_dto = UpdateOrderItemDTO(
                order_id=order_id,
                product_id=input_dto.product_id,
                product_quantity=input_dto.product_quantity + item.product_quantity
            )
            return self.update_quantity(order_id, update_dto)

        order = self._order_repo.get_by_id(order_id)
        item = OrderItem.create(order_id, input_dto.product_id, input_dto.product_quantity)
        product = self._product_repo.get_by_id(input_dto.product_id)

        order.add_order_item(item, product.price)

        self._order_repo.create_order_item(item)
        self._order_repo.update(order_id, order)
        return order

    def confirm_order(self, order_id: uuid.UUID) -> Order:
        order = self._order_repo.get_by_id(order_id)
        order.confirm_order()
        updated_order = self._order_repo.update(order_id, order)
        return updated_order

    def remove_order(self, order_id: uuid.UUID) -> None:
        order = self._order_repo.get_by_id(order_id)
        order.check_if_pending()
        self._order_repo.remove_order(order_id)

    def remove_order_item(self, order_id: uuid.UUID, product_id: uuid.UUID) -> Order:
        order = self._order_repo.get_by_id(order_id)
        item = self._order_repo.get_order_item(order_id, product_id)
        product = self._product_repo.get_by_id(product_id)

        order.remove_order_item(item, product.price)

        self._order_repo.remove_order_item(order_id, product_id)
        updated_order = self._order_repo.update(order_id, order)
        return updated_order
