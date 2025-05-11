import json
from src.logger import logger_setup
from src.classes import Product, Category

# from pprint import pprint


logger = logger_setup("utils")


def get_products_from_json(path: str) -> list[dict]:
    """Прочитать json-файл по указанному пути, вернуть список категорий и продуктов"""
    # Если try не выполнится, функция вернет пустой список
    data = []
    try:
        # Пробуем открыть файл
        logger.info(f"Считываем файл {path}")
        with open(path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Проверка структуры данных
        logger.info("Проверяем структуру считанных данных в файле")
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            logger.info("Успешно загружено {} записей".format(len(data)))
        else:
            logger.warning("Файл имеет некорректную структуру")
            data = []

    except FileNotFoundError:
        logger.error("Файл не найден")
    except json.JSONDecodeError:
        logger.error("Ошибка разбора JSON")
    except Exception as e:
        logger.error(f"Произошла ошибка: {str(e)}")
    logger.info("Завершение обработки файла")
    return data

def add_products(product_list: list[dict]) -> list:
    result = []
    for category in product_list:
        p_list =[]
        for product in category['products']:
            p_list.append(Product(**product))
        result.append(Category(name=category["name"], description=category["description"], products=p_list))
    return result
