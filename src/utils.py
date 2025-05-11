import json
from src.logger import logger_setup

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


