from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def quick_sort(arr, start=0, end=None, iteration=0, enable_visualization=True, update_rate=10):
    """
    Реализация быстрой сортировки (Quick Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - start: начальный индекс
    - end: конечный индекс
    - iteration: текущая итерация для визуализации
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления визуализации
    """
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return iteration

    # Разделяем массив относительно опорного элемента
    pivot_index = partition(arr, start, end)
    iteration += 1

    # Визуализируем процесс после разделения по опорному элементу
    visualize_sorting(arr, f"Разделение по опорному элементу {arr[pivot_index]}", iteration, update_rate,
                      enable_visualization)

    # Рекурсивно сортируем левую часть
    iteration = quick_sort(arr, start, pivot_index - 1, iteration, enable_visualization, update_rate)

    # Рекурсивно сортируем правую часть
    iteration = quick_sort(arr, pivot_index + 1, end, iteration, enable_visualization, update_rate)

    # Визуализируем состояние после полной сортировки массива
    visualize_sorting(arr, f"Часть отсортирована", iteration, update_rate, enable_visualization)

    return iteration


def partition(arr, start, end):
    """
    Функция для разделения массива на части относительно опорного элемента (pivot).

    Parameters:
    - arr: массив для сортировки
    - start: начальный индекс
    - end: конечный индекс
    """
    pivot = arr[end]  # Опорный элемент
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Обмен элементов
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# Финализация визуализации
def finalize_visualization(enable_visualization=True):
    if enable_visualization:
        plt.show(block=True)
