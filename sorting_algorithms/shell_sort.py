# sorting_algorithms/shell_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    logging.info(f"Начальный массив: {arr}")
    plt.ion()
    fig = plt.figure()

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                visualize_sorting(arr, f"Сдвиг элемента {arr[j]} для вставки")
            arr[j] = temp
        gap //= 2
        visualize_sorting(arr, f"Уменьшение разрыва до {gap}")

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
