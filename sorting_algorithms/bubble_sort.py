# sorting_algorithms/bubble_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging
import time

def bubble_sort(arr):
    """
    Реализация сортировки пузырьком с визуализацией процесса и логированием.

    Алгоритм проходит по массиву и меняет местами соседние элементы, если они стоят в неправильном порядке.
    Самый большой элемент "всплывает" к концу массива на каждой итерации.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    # Начало замера времени выполнения алгоритма
    start_time = time.time()

    plt.ion()  # Включение интерактивного режима для matplotlib
    fig = plt.figure()

    # Внешний цикл для прохода по всем элементам
    for i in range(n):
        swapped = False  # Флаг для отслеживания перестановок
        logging.debug(f"Начало {i+1}-й итерации. Массив: {arr}")

        # Внутренний цикл для сравнения и обмена элементов
        for j in range(0, n - i - 1):
            logging.debug(f"Сравнение элементов {arr[j]} и {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                # Если текущий элемент больше следующего, меняем их местами
                logging.debug(f"Обмен элементов {arr[j]} и {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Установка флага, так как произошла перестановка

                # Визуализируем текущее состояние массива после обмена
                visualize_sorting(arr, f"Итерация {i+1}, обмен {arr[j]} и {arr[j+1]}")

        # Если ни одной перестановки не произошло, значит массив уже отсортирован
        if not swapped:
            logging.info(f"Массив отсортирован досрочно на {i+1}-й итерации.")
            break

        logging.debug(f"Массив после {i+1}-й итерации: {arr}")

    # Конец замера времени
    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")

    # Финальная визуализация отсортированного массива
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)  # Оставляем график на экране
    return arr
