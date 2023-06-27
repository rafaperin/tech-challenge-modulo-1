from src.config.errors import DomainError, ResourceNotFound


class CustomerError(DomainError):
    @classmethod
    def invalid_cpf(cls) -> "CustomerError":
        return cls("Provided id is not correct according to the ObjectId standard!")


class CustomerNotFound(ResourceNotFound):
    pass


class ExportError(DomainError):
    pass
