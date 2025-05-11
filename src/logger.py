import logging
import os
from logging import Logger


def logger_setup(filename: str) -> Logger:
    """Настройка универсального логгера, форматтера и хэндлера"""
    base_dir = os.path.dirname(os.path.abspath(__file__))  # ← директория с logger_setup.py
    # print(base_dir)
    log_dir = os.path.abspath(os.path.join(base_dir, "..", "logs"))
    # log_dir = os.path.join(base_dir, "..", "logs")
    # print(log_dir)
    os.makedirs(log_dir, exist_ok=True)

    file_path = os.path.join(log_dir, f"{filename}.log")
    # print(file_path)
    logger = logging.getLogger(filename)

    # Чтобы не дублировать хендлеры при повторном вызове
    if not logger.handlers:
        file_handler = logging.FileHandler(file_path, "w", encoding="utf-8")
        file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

    return logger
