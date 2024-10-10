# sorting_algorithms/selection_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging
import time

def selection_sort(arr):
    """
    Реализация сортировки выбором с визуализацией и логированием.

    Алгоритм находит минимальный элемент в неотсортированной части массива и перемещает его в начало.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    # Начало замера времени выполнения
    start_time = time.time()
    plt.ion()
    fig = plt.figure()

    # Внешний цикл для прохода по элементам массива
    for i in range(n):
        min_idx = i  # Предполагаем, что текущий элемент — минимальный
        logging.debug(f"Начало {i+1}-й итерации. Ищем минимальный элемент в оставшейся части массива.")

        # Поиск минимального элемента в неотсортированной части массива
        for j in range(i + 1, n):
            logging.debug(f"Сравниваем текущий минимальный элемент {arr[min_idx]} с {arr[j]}")
            if arr[j] < arr[min_idx]:
                min_idx = j  # Обновляем индекс минимального элемента
                logging.debug(f"Новый минимальный элемент: {arr[min_idx]}")

        # Меняем текущий элемент с найденным минимальным
        logging.debug(f"Меняем местами {arr[i]} и {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualize_sorting(arr, f"Итерация {i+1}, минимальный элемент {arr[i]}")

    # Конец замера времени
    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
