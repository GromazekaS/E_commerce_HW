from tests.conftest import products_list
from pprint import pprint


class Product:
    name: str
    description: str
    __price: float
    quantity: int
    product_names: list[str]
    products_list: list

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, kwargs: dict, search_list: list | None = None ):
        """Добавление нового продукта с проверкой наличия такого же в списке"""
        if search_list:
            for p in search_list:
                if p.name == kwargs['name']:
                    # Убираем из списка совпадающий товар и объединяем в один (суммируем количество)
                    p = search_list.pop(search_list.index(p))
                    p.quantity += kwargs['quantity']
                    p.price = max(p.price, kwargs['price'])
                    return p
        return Product(**kwargs)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if self.__price > new_price:
                answer = input(f"Предложенная цена {new_price} меньше цены товара {self.__price}"
                               f"Подтвердить снижение стоимости товара {self.name}? Да (y)/ Нет (n): ")
                if answer in ['y', 'Y']:
                    self.__price = new_price
            else: self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")



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
        """Добавление продукта в категорию с инкрементом количества продуктов в категории"""
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
