# sorting_algorithms/bubble_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging
import time

def bubble_sort(arr):
    """
    Сортировка пузырьком с визуализацией и замером времени выполнения
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    start_time = time.time()  # Замер времени начала сортировки
    plt.ion()  # Включение интерактивного режима графика
    fig = plt.figure()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            logging.debug(f"Сравниваем {arr[j]} и {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                logging.debug(f"Меняем местами {arr[j]} и {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                visualize_sorting(arr, f"Итерация {i+1}, обмен {arr[j]} и {arr[j+1]}")
        if not swapped:
            break

    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
