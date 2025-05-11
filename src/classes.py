from tests.conftest import products_list
from pprint import pprint


class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_names: list[str]
    products_list: list

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта класса Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, kwargs, search_list: list | None = None ):
        """Добавление нового продукта с проверкой наличия такого же в списке"""
        if search_list:
            for p in search_list:
                if p.name == kwargs['name']:
                    p.quantity += kwargs['quantity']
                    p.price = max(p.price, kwargs['price'])
                    return p
        return Product(**kwargs)



class Category:
    name: str
    description: str
    __products: list[Product]
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализация объекта класса Category"""
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

    @property
    def search_list(self) -> list[Product]:
        return self.__products
