from src.config.errors import DomainError, ResourceNotFound


class CustomerError(DomainError):
    @classmethod
    def invalid_cpf(cls) -> "CustomerError":
        return cls("Provided cpf is not valid!")


class ProductError(DomainError):
    @classmethod
    def invalid_category(cls) -> "ProductError":
        return cls("Provided category is not valid!")


class OrderError(DomainError):
    @classmethod
    def invalid_category(cls) -> "OrderError":
        return cls("Provided order is not valid!")


class OrderItemError(DomainError):
    @classmethod
    def modification_blocked(cls) -> "OrderItemError":
        return cls("Order already confirmed, modification not allowed!")


class CustomerNotFound(ResourceNotFound):
    pass


class ExportError(DomainError):
    pass
