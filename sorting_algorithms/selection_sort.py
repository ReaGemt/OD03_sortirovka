# sorting_algorithms/selection_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import time
import logging


def selection_sort(arr):
    n = len(arr)
    start_time = time.time()
    plt.ion()
    fig = plt.figure()

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualize_sorting(arr, f"Итерация {i + 1}, минимальный элемент {arr[i]}")

    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
