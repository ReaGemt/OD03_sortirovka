# sorting_algorithms/insertion_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import time
import logging

def insertion_sort(arr):
    start_time = time.time()
    plt.ion()
    fig = plt.figure()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        visualize_sorting(arr, f"Итерация {i+1}, вставка элемента {key}")

    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
