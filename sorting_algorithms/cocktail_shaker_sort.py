# sorting_algorithms/cocktail_shaker_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def cocktail_shaker_sort(arr):
    """
    Реализация шейкерной сортировки с визуализацией и логированием.

    Алгоритм представляет собой модификацию пузырьковой сортировки, проходя по массиву
    слева направо, а затем обратно справа налево, перемещая большие элементы вправо, а маленькие — влево.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")
    start = 0  # Начальный индекс
    end = n - 1  # Конечный индекс

    plt.ion()
    fig = plt.figure()

    # Основной цикл: сортируем в обе стороны
    while start <= end:
        swapped = False
        logging.debug(f"Проход слева направо. Начальный индекс: {start}, Конечный индекс: {end}")

        # Проход слева направо
        for i in range(start, end):
            logging.debug(f"Сравниваем элементы {arr[i]} и {arr[i+1]}")
            if arr[i] > arr[i + 1]:
                logging.debug(f"Обмен {arr[i]} и {arr[i+1]}")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr, f"Обмен {arr[i]} и {arr[i+1]}")

        # Если не было обменов, сортировка завершена
        if not swapped:
            logging.info("Массив уже отсортирован. Завершение.")
            break
        swapped = False
        end -= 1  # Уменьшаем конец, так как последний элемент уже отсортирован

        logging.debug(f"Проход справа налево. Начальный индекс: {start}, Конечный индекс: {end}")

        # Проход справа налево
        for i in range(end - 1, start - 1, -1):
            logging.debug(f"Сравниваем элементы {arr[i]} и {arr[i+1]}")
            if arr[i] > arr[i + 1]:
                logging.debug(f"Обмен {arr[i]} и {arr[i+1]}")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                visualize_sorting(arr, f"Обмен {arr[i]} и {arr[i+1]}")

        start += 1  # Увеличиваем начало, так как первый элемент уже отсортирован

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)  # Оставляем график на экране
    return arr
