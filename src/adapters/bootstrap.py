from kink import di

from src.adapters.repositories.order.order_orm import Orders
from src.adapters.repositories.order.postgres_order_repository import PostgresDBOrderRepository
from src.adapters.repositories.order_items.order_item_orm import Order_Items
from src.adapters.repositories.order_items.postgres_order_item_repository import PostgresDBOrderItemRepository
from src.adapters.repositories.product.postgres_product_repository import PostgresDBProductRepository
from src.adapters.repositories.product.product_orm import Products
from src.adapters.services.customer_service import CustomerService
from src.adapters.repositories.customer.customer_orm import Customers
from src.adapters.services.order_items_service import OrderItemService
from src.adapters.services.order_service import OrderService
from src.adapters.services.product_service import ProductService
from src.domain.ports.repositories.customer_repository import ICustomerRepository
from src.adapters.repositories.customer.postgres_customer_repository import PostgresDBCustomerRepository
from src.domain.ports.repositories.order_items_repository import IOrderItemsRepository
from src.domain.ports.repositories.order_repository import IOrderRepository
from src.domain.ports.repositories.product_repository import IProductRepository


def bootstrap_di() -> None:
    customer_repository = PostgresDBCustomerRepository(Customers)
    di[ICustomerRepository] = customer_repository
    di[CustomerService] = CustomerService(customer_repository)

    product_repository = PostgresDBProductRepository(Products)
    di[IProductRepository] = product_repository
    di[ProductService] = ProductService(product_repository)

    orders_repository = PostgresDBOrderRepository(Orders, Order_Items)
    di[IOrderRepository] = orders_repository
    di[OrderService] = OrderService(orders_repository)
    #
    # order_items_repository = PostgresDBOrderItemRepository(Order_Items)
    # di[IOrderItemsRepository] = order_items_repository
    # di[OrderItemService] = OrderItemService(order_items_repository)
