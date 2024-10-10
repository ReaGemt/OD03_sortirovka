from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def insertion_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки вставками с возможностью включения/выключения визуализации
    и контролем частоты обновления графиков.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    # Включаем интерактивный режим matplotlib
    plt.ion() if enable_visualization else None
    iteration = 0  # Счётчик для отслеживания итераций

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Перемещение элементов, которые больше ключа, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            iteration += 1

            # Визуализируем на каждой итерации, если включена визуализация
            visualize_sorting(arr, f"Итерация {i}, вставка элемента {key}", iteration, update_rate,
                              enable_visualization)

        arr[j + 1] = key

        # Визуализируем после вставки ключевого элемента на правильную позицию
        iteration += 1
        visualize_sorting(arr, f"Вставка {key} завершена", iteration, update_rate, enable_visualization)

    logging.info(f"Конечный отсортированный массив: {arr}")

    # Финальная визуализация после завершения сортировки
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1,
                      enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None

    return arr
