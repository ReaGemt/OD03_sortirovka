# sorting_algorithms/main.py
import time
import logging
import matplotlib
from PIL import Image

# Отключаем DEBUG-логи от PIL (используется для работы с изображениями в matplotlib)
pil_logger = logging.getLogger('PIL')
pil_logger.setLevel(logging.WARNING)

# Отключаем DEBUG-логи от matplotlib
matplotlib_logger = logging.getLogger('matplotlib')
matplotlib_logger.setLevel(logging.WARNING)

# Импорт всех алгоритмов
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort
from cocktail_shaker_sort import cocktail_shaker_sort
from shell_sort import shell_sort

# Массивы для тестирования
arrays = {
    "Bubble Sort": [64, 34, 25, 12, 22, 11, 90],
    "Selection Sort": [64, 25, 12, 22, 11],
    "Quick Sort": [3, 6, 8, 10, 1, 2, 1],
    "Insertion Sort": [12, 11, 13, 5, 6],
    "Merge Sort": [12, 11, 13, 5, 6, 7],
    "Heap Sort": [12, 11, 13, 5, 6, 7],
    "Counting Sort": [4, 2, 2, 8, 3, 3, 1],
    "Radix Sort": [170, 45, 75, 90, 802, 24, 2, 66],
    "Cocktail Shaker Sort": [5, 1, 4, 2, 8, 0, 2],
    "Shell Sort": [12, 34, 54, 2, 3],
}


def run_all_sorts():
    """
    Функция для запуска всех алгоритмов сортировки по очереди с таймаутом и логированием.

    Алгоритмы сортируются по очереди, и каждый массив тестируется на одном из алгоритмов. После каждого
    запуска предусмотрена пауза, чтобы визуализация одного алгоритма не мешала следующему.
    """
    for sort_name, array in arrays.items():
        print(f"\nЗапуск {sort_name}")
        logging.info(f"Запуск алгоритма {sort_name} с исходным массивом: {array}")

        # Копируем исходный массив для тестирования, чтобы каждый раз сортировать оригинал
        array_copy = array.copy()

        # Выбор и запуск алгоритма сортировки по его названию
        if sort_name == "Bubble Sort":
            bubble_sort(array_copy)
        elif sort_name == "Selection Sort":
            selection_sort(array_copy)
        elif sort_name == "Quick Sort":
            quick_sort(array_copy)
        elif sort_name == "Insertion Sort":
            insertion_sort(array_copy)
        elif sort_name == "Merge Sort":
            merge_sort(array_copy)
        elif sort_name == "Heap Sort":
            heap_sort(array_copy)
        elif sort_name == "Counting Sort":
            counting_sort(array_copy)
        elif sort_name == "Radix Sort":
            radix_sort(array_copy)
        elif sort_name == "Cocktail Shaker Sort":
            cocktail_shaker_sort(array_copy)
        elif sort_name == "Shell Sort":
            shell_sort(array_copy)

        # Таймаут в 3 секунды перед запуском следующего алгоритма
        print(f"Ожидание 5 секунд перед запуском следующего алгоритма...\n")
        logging.info(f"Ожидание 5 секунд перед запуском следующего алгоритма {sort_name}.")
        time.sleep(5)


if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    run_all_sorts()
