import datetime
import uuid
from dataclasses import dataclass

class OrderStatus:
    PENDING = "pendente"
    CONFIRMED = "confirmado"
    IN_PROGRESS = "em preparo"
    READY = "pronto"
    FINALIZED = "finalizado"


@dataclass
class Order:
    order_id: uuid.UUID
    customer_id: uuid.UUID
    creation_date: datetime.datetime
    order_total: float
    status: str

    @classmethod
    def create_new_order(cls, customer_id: uuid.UUID) -> "Order":
        order_id = uuid.uuid4()
        return cls(order_id, customer_id, datetime.datetime.utcnow(), 0.0, OrderStatus.PENDING)

    def calculate_order_total(self, order_items: list) -> float:
        total = 0.0
        for item in order_items:
            total += item.product_quantity * item.product_price
        return total

    def update_order_total(self, new_total: float) -> None:
        self.order_total = new_total

    def confirm_order(self) -> None:
        self.status = OrderStatus.CONFIRMED


def order_factory(
     order_id: uuid.UUID,
     customer_id: uuid.UUID,
     creation_date: datetime.datetime,
     order_total: float,
     status: str
) -> Order:
    return Order(
        order_id=order_id,
        customer_id=customer_id,
        creation_date=creation_date,
        order_total=order_total,
        status=status
    )
