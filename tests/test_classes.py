# import pytest
from src.classes import Product, Category


def test_product(products_list: list) -> None:
    prod = Product(**products_list[0]["products"][1])
    assert prod.name == "Iphone 15"
    assert prod.description == "512GB, Gray space"
    assert prod.price == 210000.0
    assert prod.quantity == 8


def test_category(products_list: list) -> None:
    category1 = Category(name=products_list[0]["name"], description=products_list[0]["description"], products=[])
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category1.products == []


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
