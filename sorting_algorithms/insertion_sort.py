# sorting_algorithms/insertion_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging
import time

def insertion_sort(arr):
    """
    Реализация сортировки вставками с визуализацией и логированием.

    Алгоритм проходит по каждому элементу и вставляет его на нужное место в отсортированной части массива.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    logging.info(f"Начальный массив: {arr}")

    # Начало замера времени
    start_time = time.time()
    plt.ion()
    fig = plt.figure()

    # Проход по элементам массива, начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1
        logging.debug(f"Вставляем элемент {key}")

        # Сдвиг элементов вправо, чтобы найти правильное место для вставки
        while j >= 0 and arr[j] > key:
            logging.debug(f"Сдвигаем {arr[j]} вправо")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        visualize_sorting(arr, f"Итерация {i+1}, вставка элемента {key}")

    # Конец замера времени
    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
