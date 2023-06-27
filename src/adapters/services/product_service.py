from kink import inject

from src.domain.model.product_schemas import (
    ChangeProductDTO,
    CreateProductDTO,
)
from src.domain.model.product_model import Product, product_factory
from src.domain.ports.repositories.product_repository import IProductRepository
from src.domain.ports.services.product_service import ProductServiceInterface


@inject
class ProductService(ProductServiceInterface):
    def __init__(self, product_repo: IProductRepository) -> None:
        self._product_repo = product_repo

    def get_by_id(self, id: int):
        result = self._product_repo.get_by_id(id)
        product = product_factory(
            result.name,
            result.description,
            result.category,
            result.price,
            result.image_url,
        )
        return product

    def get_all(self):
        result = self._product_repo.get_all()
        products = []
        for obj in result:
            product = product_factory(
                obj.name,
                obj.description,
                obj.category,
                obj.price,
                obj.image_url,
            )
            products.append(product)
        return products

    def get_all_by_category(self, category: str):
        result = self._product_repo.get_all_by_category(category)
        products = []
        for obj in result:
            product = product_factory(
                obj.name,
                obj.description,
                obj.category,
                obj.price,
                obj.image_url,
            )
            products.append(product)
        return products

    def create(self, input_dto: CreateProductDTO) -> Product:
        product = Product.create(
            input_dto.name,
            input_dto.description,
            input_dto.category,
            input_dto.price,
            input_dto.image_url,
        )
        self._product_repo.create(product)
        return product

    def update(self, id: int, input_dto: ChangeProductDTO) -> Product:
        product = self._product_repo.get_by_id(id)
        if input_dto.name or input_dto.description or input_dto.category:
            product.change_product_data(input_dto.name, input_dto.description, input_dto.category)
        if input_dto.price:
            product.change_price(input_dto.price)
        if input_dto.image_url:
            product.change_image_url(input_dto.image_url)

        updated_product = self._product_repo.update(product)
        return updated_product

    def remove(self, id: int) -> None:
        self._product_repo.remove(id)
