from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    category: str
    price: float
    image_url: str

    @classmethod
    def create(cls, name: str, description: str, category: str, price: float, image_url: str) -> "Product":
        return cls(name, description, category, price, image_url)

    def change_product_data(self, new_name: str, new_description: str, new_category: str) -> None:
        self.name = new_name
        self.description = new_description
        self.category = new_category

    def change_price(self, new_price: float) -> None:
        self.price = new_price

    def change_image_url(self, new_image_url: str) -> None:
        self.image_url = new_image_url


def product_factory(name: str, description: str, category: str, price: float, image_url: str) -> Product:
    return Product(
        name=name,
        description=description,
        category=category,
        price=price,
        image_url=image_url,
    )
