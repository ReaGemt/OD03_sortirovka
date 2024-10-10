# sorting_algorithms/heap_sort.py
from visualization import visualize_sorting
import logging

def heap_sort(arr):
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        logging.debug(f"Меняем местами {arr[0]} и {arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        visualize_sorting(arr, f"Извлечение максимального элемента {arr[i]}")
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        logging.debug(f"Меняем местами {arr[i]} и {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        visualize_sorting(arr, f"Перестройка кучи на индексе {i}")
