from abc import ABC

from src.domain.model.product_schemas import CreateProductDTO, ChangeProductDTO
from src.domain.model.product_model import Product
from src.domain.ports.repositories.product_repository import IProductRepository


class ProductServiceInterface(ABC):
    def __init__(self, product_repo: IProductRepository) -> None:
        raise NotImplementedError

    def get_by_id(self, id: str):
        pass

    def get_all(self):
        pass

    def get_all_by_category(self, category: str):
        pass

    def create(self, input_dto: CreateProductDTO) -> Product:
        pass

    def update(self, id: int, input_dto: ChangeProductDTO) -> Product:
        pass

    def remove(self, id: int) -> None:
        pass

