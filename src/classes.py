from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    @abstractmethod
    def price(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, kwargs: dict, search_list: list | None = None):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct):
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

    def __str__(self) -> str:
        """Вывод в консоль информации об объекте"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other: "Product") -> float:
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError("Возникла ошибка TypeError при попытке сложения")

    @classmethod
    def new_product(cls, kwargs: dict, search_list: list | None = None) -> Any:
        """Добавление нового продукта с проверкой наличия такого же в списке"""
        if search_list:
            for p in search_list:
                if p.name == kwargs["name"]:
                    # Убираем из списка совпадающий товар и объединяем в один (суммируем количество)
                    p = search_list.pop(search_list.index(p))
                    p.quantity += kwargs["quantity"]
                    p.price = max(p.price, kwargs["price"])
                    return p
        return Product(**kwargs)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if self.__price > new_price:
                answer = input(
                    f"Предложенная цена {new_price} меньше цены товара {self.__price}"
                    f"Подтвердить снижение стоимости товара {self.name}? Да (y)/ Нет (n): "
                )
                if answer in ["y", "Y"]:
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    def __str__(self) -> str:
        """Вывод в консоль информации об объекте"""
        quantity = 0
        for p in self.__products:
            quantity += p.quantity
        return f"{self.name}, количество продуктов: {quantity} шт.\n"

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию с инкрементом количества продуктов в категории"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Возникла ошибка TypeError при попытке добавления не-продукта")

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def search_list(self) -> list[Product]:
        return self.__products

    def get_products(self) -> list[Product]:
        return self.__products


class Audit:
    def __init__(self, category: Category):
        self.products = category.get_products()
        self.counter = 0

    def __iter__(self) -> Any:
        return self

    def __next__(self) -> Product:
        if self.counter < len(self.products):
            self.counter += 1
            return self.products[self.counter - 1]
        else:
            raise StopIteration
