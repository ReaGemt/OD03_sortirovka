# sorting_algorithms/selection_sort.py
from visualization import visualize_sorting
import logging
import time
import matplotlib.pyplot as plt

def selection_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки выбором с возможностью включения/выключения визуализации
    и контролем частоты обновления графиков.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    start_time = time.time()  # Замер времени начала сортировки
    plt.ion()  # Включение интерактивного режима для matplotlib
    fig = plt.figure() if enable_visualization else None

    iteration = 0  # Для отслеживания количества итераций

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            iteration += 1
            logging.debug(f"Сравнение {arr[j]} с текущим минимальным элементом {arr[min_idx]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
                logging.debug(f"Новый минимальный элемент: {arr[min_idx]}")

        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Обмен
        logging.debug(f"Меняем местами {arr[i]} и {arr[min_idx]}")
        visualize_sorting(arr, f"Итерация {i + 1}, минимальный элемент {arr[i]}", iteration, update_rate,
                          enable_visualization)

    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")

    # Финальная визуализация
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1,
                      enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
