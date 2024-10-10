from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging
import time


def bubble_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки пузырьком с возможностью включения/выключения визуализации
    и контролем частоты обновления графиков.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    start_time = time.time()  # Замер времени начала сортировки

    plt.ion()  # Включение интерактивного режима для matplotlib, если визуализация включена
    fig = plt.figure() if enable_visualization else None

    iteration = 0  # Для отслеживания количества итераций
    for i in range(n):
        swapped = False  # Флаг для отслеживания перестановок
        logging.debug(f"Начало {i + 1}-й итерации. Массив: {arr}")

        for j in range(0, n - i - 1):
            iteration += 1  # Увеличиваем счётчик итераций
            logging.debug(f"Сравнение элементов {arr[j]} и {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                logging.debug(f"Обмен элементов {arr[j]} и {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Установка флага, так как произошла перестановка

                # Визуализируем текущее состояние массива после обмена раз в N итераций
                visualize_sorting(arr, f"Итерация {i + 1}, обмен {arr[j]} и {arr[j + 1]}", iteration, update_rate,
                                  enable_visualization)

        if not swapped:
            logging.info(f"Массив отсортирован досрочно на {i + 1}-й итерации.")
            break

    end_time = time.time()
    total_time = end_time - start_time  # Вычисляем общее время сортировки
    logging.info(f"Время выполнения: {total_time:.4f} секунд")

    # Финальная визуализация после завершения сортировки
    if enable_visualization:
        plt.clf()  # Очищаем график перед финальной визуализацией
        plt.bar(range(len(arr)), arr, color='blue')  # Отображаем финальный отсортированный массив
        plt.title(f"Конечный отсортированный массив\nВремя выполнения: {total_time:.4f} секунд")  # Добавляем время в заголовок
        plt.draw()
        plt.show(block=True)

    return arr
