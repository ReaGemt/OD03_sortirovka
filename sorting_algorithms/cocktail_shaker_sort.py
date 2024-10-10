# sorting_algorithms/cocktail_shaker_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def cocktail_shaker_sort(arr):
    """
    Реализация шейкерной сортировки с визуализацией и логированием.

    Алгоритм проходит по массиву слева направо и справа налево, попеременно двигая
    максимальные и минимальные элементы к краям.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    start = 0  # Начало прохода
    end = n - 1  # Конец прохода
    logging.info(f"Начальный массив: {arr}")

    plt.ion()
    fig = plt.figure()

    # Проходы по массиву слева направо и справа налево
    while start <= end:
        swapped = False

        # Проход слева направо
        logging.debug(f"Проход слева направо, от {start} до {end}")
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                logging.debug(f"Меняем местами {arr[i]} и {arr[i+1]}")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr, f"Обмен {arr[i]} и {arr[i+1]}")

        if not swapped:
            logging.info("Массив отсортирован. Перестановок не произошло.")
            break
        swapped = False
        end -= 1

        # Проход справа налево
        logging.debug(f"Проход справа налево, от {end} до {start}")
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                logging.debug(f"Меняем местами {arr[i]} и {arr[i+1]}")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr, f"Обмен {arr[i]} и {arr[i+1]}")

        start += 1

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
