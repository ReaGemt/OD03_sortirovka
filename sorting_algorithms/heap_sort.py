# sorting_algorithms/heap_sort.py
from visualization import visualize_sorting
import logging

def heap_sort(arr):
    """
    Реализация пирамидальной сортировки с визуализацией и логированием.

    Алгоритм преобразует массив в кучу (heap), затем последовательно извлекает наибольшие элементы из кучи.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        logging.debug(f"Построение кучи: обработка индекса {i}")
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n-1, 0, -1):
        logging.debug(f"Меняем местами {arr[0]} и {arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        visualize_sorting(arr, f"Извлечение максимального элемента {arr[i]}")
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    """
    Преобразует поддерево массива в кучу, начиная с корня (i).

    Parameters:
    - arr: массив
    - n: количество элементов в куче
    - i: индекс корня поддерева
    """
    largest = i  # Инициализация наибольшего элемента как корня
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок больше наибольшего на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        logging.debug(f"Меняем местами {arr[i]} и {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        visualize_sorting(arr, f"Перестройка кучи на индексе {i}")
