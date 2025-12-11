import shutil
from pathlib import Path


def clear_allure_results():
    """Очищение результатов модуля allure-results"""
    allure_dir = Path("allure-results")

    if allure_dir.exists():
        shutil.rmtree(allure_dir)

    allure_dir.mkdir(exist_ok=True)
