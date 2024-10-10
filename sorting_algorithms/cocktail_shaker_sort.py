# sorting_algorithms/cocktail_shaker_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def cocktail_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    logging.info(f"Начальный массив: {arr}")
    plt.ion()
    fig = plt.figure()

    while start <= end:
        swapped = False

        # Проход слева направо
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr, f"Обмен {arr[i]} и {arr[i+1]}")

        if not swapped:
            break
        swapped = False
        end -= 1

        # Проход справа налево
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr, f"Обмен {arr[i]} и {arr[i+1]}")

        start += 1

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
