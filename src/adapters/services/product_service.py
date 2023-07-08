import uuid

from kink import inject

from src.config.errors import ResourceNotFound
from src.domain.model.product.product_schemas import (
    ChangeProductDTO,
    CreateProductDTO,
)
from src.domain.model.product.product_model import Product, product_factory
from src.domain.ports.repositories.product_repository import IProductRepository
from src.domain.ports.services.product_service import ProductServiceInterface


@inject
class ProductService(ProductServiceInterface):
    def __init__(self, product_repo: IProductRepository) -> None:
        self._product_repo = product_repo

    def get_by_id(self, product_id: uuid.UUID):
        result = self._product_repo.get_by_id(product_id)
        if not result:
            raise ResourceNotFound
        else:
            product = product_factory(
                result.product_id,
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
                obj.product_id,
                obj.name,
                obj.description,
                obj.category,
                obj.price,
                obj.image_url,
            )
            products.append(product)
        return products

    def get_all_by_category(self, category: str):
        result = self._product_repo.get_all_by_category(category.lower().capitalize())
        products = []
        for obj in result:
            product = product_factory(
                obj.product_id,
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

    def update(self, product_id: uuid.UUID, input_dto: ChangeProductDTO) -> Product:
        product = self._product_repo.get_by_id(product_id)
        if input_dto.name:
            product.change_product_name(input_dto.name)
        if input_dto.description:
            product.change_product_description(input_dto.description)
        if input_dto.category:
            product.change_product_category(input_dto.category)
        if input_dto.price:
            product.change_price(input_dto.price)
        if input_dto.image_url:
            product.change_image_url(input_dto.image_url)

        updated_product = self._product_repo.update(product)
        return updated_product

    def remove(self, product_id: uuid.UUID) -> None:
        self._product_repo.remove(product_id)
