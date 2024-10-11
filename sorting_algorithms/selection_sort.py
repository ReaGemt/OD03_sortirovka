from visualization import visualize_sorting
import logging
import time
import matplotlib.pyplot as plt

def selection_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки выбором с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")
    start_time = time.time()  # Замер времени начала сортировки

    iteration = 0
    for i in range(n):
        min_idx = i  # Предполагаем, что текущий элемент минимальный
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Находим индекс минимального элемента

        # Меняем местами минимальный элемент и текущий
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        iteration += 1
        # Визуализация после каждого обмена
        visualize_sorting(arr, f"Итерация {i+1}: выбор минимального элемента", iteration, update_rate, enable_visualization)

    end_time = time.time()  # Замер времени окончания сортировки
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
