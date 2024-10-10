# sorting_algorithms/shell_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def shell_sort(arr):
    """
    Реализация сортировки Шелла с визуализацией и логированием.

    Алгоритм улучшает сортировку вставками, добавляя возможность сравнивать элементы,
    находящиеся на большом расстоянии друг от друга.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    gap = n // 2  # Инициализация разрыва между элементами
    logging.info(f"Начальный массив: {arr}")

    plt.ion()
    fig = plt.figure()

    # Уменьшаем разрыв на каждом этапе
    while gap > 0:
        logging.debug(f"Текущий разрыв: {gap}")

        # Проход по элементам массива
        for i in range(gap, n):
            temp = arr[i]
            j = i
            logging.debug(f"Вставка элемента {temp} на правильное место с разрывом {gap}")

            # Сдвиг элементов вправо, пока не найдём правильное место для temp
            while j >= gap and arr[j - gap] > temp:
                logging.debug(f"Сдвиг {arr[j-gap]} вправо")
                arr[j] = arr[j - gap]
                j -= gap
                visualize_sorting(arr, f"Сдвиг элемента {arr[j-gap]}")

            arr[j] = temp
            visualize_sorting(arr, f"Вставка элемента {temp} на правильное место")

        # Уменьшаем разрыв
        gap //= 2
        logging.debug(f"Уменьшение разрыва до {gap}")

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
