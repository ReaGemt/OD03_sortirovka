# sorting_algorithms/quick_sort.py
from visualization import visualize_sorting
import logging

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr

    pivot_index = partition(arr, start, end)
    visualize_sorting(arr, f"Разделение с опорным элементом {arr[pivot_index]}")
    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        logging.debug(f"Сравниваем {arr[j]} с опорным элементом {pivot}")
        if arr[j] < pivot:
            i += 1
            logging.debug(f"Меняем местами {arr[i]} и {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            visualize_sorting(arr, f"Перестановка: {arr[i]} и {arr[j]}")
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
