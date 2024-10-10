# sorting_algorithms/counting_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def counting_sort(arr):
    """
    Реализация сортировки подсчётом с визуализацией и логированием.

    Алгоритм работает, подсчитывая количество вхождений каждого уникального элемента в массиве, а затем
    размещает элементы в итоговый массив на основе этих подсчетов.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    logging.info(f"Начальный массив: {arr}")

    # Поиск максимального и минимального значений в массиве
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Инициализация вспомогательных массивов
    count = [0] * range_of_elements  # Массив для подсчёта количества элементов
    output = [0] * len(arr)  # Массив для хранения отсортированных элементов

    # Подсчёт количества каждого элемента
    logging.debug(f"Подсчёт количества элементов...")
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        visualize_sorting(count, f"Обновление счётчика для элемента {arr[i]}")

    # Модификация count для хранения конечных позиций элементов
    logging.debug(f"Модификация счётчика для позиций...")
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        visualize_sorting(count, "Обновление позиции для элемента")

    # Построение выходного массива на основе count
    logging.debug(f"Построение отсортированного массива...")
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        visualize_sorting(output, f"Вставка элемента {arr[i]} на правильное место")

    logging.info(f"Конечный отсортированный массив: {output}")
    visualize_sorting(output, "Конечный отсортированный массив")
    plt.show(block=True)
    return output
