import pytest
from src.classes import Product, Category


def test_product(products_list):
    prod = Product(**products_list[0]['products'][1])
    assert prod.name == "Iphone 15"
    assert prod.description == "512GB, Gray space"
    assert prod.price == 210000.0
    assert prod.quantity == 8


def test_category(products_list):
    category1 = Category(name=products_list[0]['name'], description=products_list[0]['description'], products=[])
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category1.products == []
    assert Category.category_count == 1
    category1 = Category(name=products_list[1]['name'], description=products_list[1]['description'], products=[])
    assert Category.category_count == 2
