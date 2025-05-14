from unittest.mock import patch

import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


def test_product(products_list: list) -> None:
    prod = Product(**products_list[0]["products"][1])
    assert prod.name == "Iphone 15"
    assert prod.description == "512GB, Gray space"
    assert prod.price == 210000.0
    assert prod.quantity == 8


def test_product_new_product(products_list: list) -> None:
    p1 = Product.new_product(products_list[0]["products"][0])
    p2 = Product.new_product(products_list[0]["products"][1])
    p3 = Product.new_product(products_list[0]["products"][2])
    assert p2.quantity == 8
    p_new = Product.new_product(products_list[0]["products"][1], [p1, p2, p3])
    # {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    assert p_new.name == "Iphone 15"
    assert p_new.description == "512GB, Gray space"
    assert p_new.price == 210000.0
    assert p_new.quantity == 16


def test_product_print(products_list: list) -> None:
    prod = Product(**products_list[0]["products"][1])
    assert str(prod) == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_product_add(products_list: list) -> None:
    p2 = Product.new_product(products_list[0]["products"][1])
    p3 = Product.new_product(products_list[0]["products"][2])
    #    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
    #    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    # 8 * 210000 = 1_680_000, 14 * 31_000 = 434_000 : 2_114_000
    assert p2 + p3 == 2_114_000.0


def test_sum_different_products() -> None:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError) as exc_info:
        print(smartphone1 + grass1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Возникла ошибка TypeError при попытке сложения"


def test_product_new_product_update_greater_price(products_list: list) -> None:
    p3 = Product.new_product(products_list[0]["products"][2])
    assert p3.price == 31000.0
    p_add = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 38000.0, "quantity": 14}
    p_new = Product.new_product(p_add, [p3])
    # {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    assert p_new.name == "Xiaomi Redmi Note 11"
    assert p_new.description == "1024GB, Синий"
    assert p_new.price == 38000.0


def test_product_new_product_from_list(products_list: list) -> None:
    p1 = Product.new_product(products_list[0]["products"][2])
    # {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
    assert p1.name == "Xiaomi Redmi Note 11"
    assert p1.description == "1024GB, Синий"
    assert p1.price == 31000.0
    assert p1.quantity == 14


def test_price_setter_accepts_price_increase() -> None:
    product = Product("Телевизор", "4K", 100000.0, 5)
    product.price = 190000.0
    assert product.price == 190000.0


def test_price_setter_accepts_price_reduction() -> None:
    product = Product("Телевизор", "4K", 100000.0, 5)

    with patch("builtins.input", return_value="y"):
        product.price = 90000.0

    assert product.price == 90000.0


def test_price_setter_rejects_price_reduction() -> None:
    product = Product("Телевизор", "4K", 100000.0, 5)

    with patch("builtins.input", return_value="n"):
        product.price = 90000.0

    assert product.price == 100000.0


def test_price_setter_negative_price() -> None:
    product = Product("Телевизор", "4K", 100000.0, 5)

    product.price = -5000.0

    assert product.price == 100000.0  # цена не изменилась


def test_category(products_list: list) -> None:
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[])
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category1.products == ""


def test_category_count(products_list: list) -> None:
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[])
    assert Category.category_count == 2
    category2 = Category(name=products_list[1]["name"], description=products_list[1]["description"], products=[])
    assert Category.category_count == 3


def test_product_count(products_list: list) -> None:
    p1 = Product(**products_list[0]["products"][0])
    p3 = Product(**products_list[0]["products"][2])
    p4 = Product(**products_list[1]["products"][0])
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[p1, p3])
    assert Category.product_count == 2
    category2 = Category(name=products_list[1]["name"], description=products_list[1]["description"], products=[p4])
    assert Category.product_count == 3


def test_category_print(products_list: list) -> None:
    prod = Product(**products_list[0]["products"][1])
    assert str(prod) == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_category_search_list(products_list: list) -> None:
    p1 = Product(**products_list[0]["products"][0])
    p2 = Product(**products_list[0]["products"][1])
    p3 = Product(**products_list[0]["products"][2])
    category1 = Category(
        name=products_list[0]["name"], description=products_list[0]["description"], products=[p1, p2, p3]
    )
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт.\n"


def test_category_products_info(products_list: list) -> None:
    p1 = Product(**products_list[0]["products"][0])
    p3 = Product(**products_list[0]["products"][2])
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[p1, p3])
    assert category1.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_add_product(products_list: list) -> None:
    Category.product_count = 0
    p1 = Product(**products_list[0]["products"][0])
    p3 = Product(**products_list[0]["products"][2])
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[p3])
    assert category1.product_count == 1
    category1.add_product(p1)
    assert category1.product_count == 2


def test_category_add_not_product(products_list: list) -> None:
    Category.product_count = 0
    p3 = Product(**products_list[0]["products"][2])
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[p3])
    with pytest.raises(TypeError) as exc_info:
        category1.add_product("Явно не товар")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Возникла ошибка TypeError при попытке добавления не-продукта"


def test_smartphone() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass() -> None:
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"
