from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def counting_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки подсчётом с возможностью включения/выключения визуализации
    и контролем частоты обновления графиков.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    # Находим максимальное значение в массиве для создания диапазона
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Массив для подсчёта элементов
    count = [0] * range_of_elements
    output = [0] * len(arr)

    plt.ion() if enable_visualization else None
    iteration = 0  # Счётчик для итераций

    # Подсчёт количества вхождений каждого элемента
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        iteration += 1
        # Визуализируем процесс подсчёта
        visualize_sorting(count, f"Итерация {iteration}: подсчёт", iteration, update_rate, enable_visualization)

    # Модифицируем массив count, чтобы хранить индексы конечных позиций элементов
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        iteration += 1
        # Визуализируем процесс модификации массива count
        visualize_sorting(count, f"Итерация {iteration}: модификация счётчика", iteration, update_rate,
                          enable_visualization)

    # Построение выходного массива
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        iteration += 1
        # Визуализируем процесс заполнения выходного массива
        visualize_sorting(output, f"Итерация {iteration}: построение выходного массива", iteration, update_rate,
                          enable_visualization)

    # Копируем отсортированный массив обратно в arr
    for i in range(len(arr)):
        arr[i] = output[i]

    logging.info(f"Конечный отсортированный массив: {arr}")

    # Финальная визуализация после завершения сортировки
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1,
                      enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None

    return arr
