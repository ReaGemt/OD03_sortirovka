# sorting_algorithms/counting_sort.py
from visualization import visualize_sorting
import logging


def counting_sort(arr):
    logging.info(f"Начальный массив: {arr}")
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        visualize_sorting(count, "Обновление счётчика элементов")

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        visualize_sorting(count, "Модификация счётчика для позиций")

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        visualize_sorting(output, f"Построение выходного массива: {arr[i]}")

    logging.info(f"Конечный отсортированный массив: {output}")
    visualize_sorting(output, "Конечный отсортированный массив")
    plt.show(block=True)
    return output
