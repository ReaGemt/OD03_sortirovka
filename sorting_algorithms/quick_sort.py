# sorting_algorithms/quick_sort.py
from visualization import visualize_sorting
import logging

def quick_sort(arr, start=0, end=None):
    """
    Реализация быстрой сортировки с логированием и визуализацией.

    Алгоритм делит массив на части, сравнивая элементы с опорным элементом (pivot).
    Затем рекурсивно сортирует левую и правую части относительно pivot.

    Parameters:
    - arr: массив для сортировки
    - start: начальный индекс
    - end: конечный индекс

    Returns:
    - Отсортированный массив
    """
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr

    logging.debug(f"Сортировка части массива от индекса {start} до {end}. Массив: {arr[start:end+1]}")

    # Выбор опорного элемента и разделение массива
    pivot_index = partition(arr, start, end)
    visualize_sorting(arr, f"Разделение с опорным элементом {arr[pivot_index]}")

    # Рекурсивная сортировка левой и правой частей массива
    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)
    return arr

def partition(arr, start, end):
    """
    Функция для разделения массива относительно опорного элемента.

    Parameters:
    - arr: массив для сортировки
    - start: начальный индекс
    - end: конечный индекс

    Returns:
    - Индекс опорного элемента после разделения
    """
    pivot = arr[end]  # Выбираем последний элемент как опорный (pivot)
    logging.debug(f"Опорный элемент выбран: {pivot}")
    i = start - 1  # Индекс для разделения элементов

    # Проход по массиву и разделение на две части: меньше и больше pivot
    for j in range(start, end):
        logging.debug(f"Сравниваем {arr[j]} с опорным элементом {pivot}")
        if arr[j] < pivot:
            i += 1
            logging.debug(f"Меняем местами {arr[i]} и {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            visualize_sorting(arr, f"Перестановка: {arr[i]} и {arr[j]}")

    # Помещаем опорный элемент на своё место
    logging.debug(f"Помещаем опорный элемент {pivot} на позицию {i+1}")
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
