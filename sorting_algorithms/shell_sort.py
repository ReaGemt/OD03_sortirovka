from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def shell_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки Шелла (Shell Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    n = len(arr)
    gap = n // 2  # Начальное значение разрыва (gap)
    iteration = 0  # Счётчик для отслеживания количества итераций

    plt.ion() if enable_visualization else None

    # Уменьшаем разрыв, пока он не станет 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Выполняем сортировку вставками для элементов, разделённых разрывом
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                iteration += 1

                # Визуализируем процесс перемещения элементов
                visualize_sorting(arr, f"Итерация {iteration}: разрыв {gap}", iteration, update_rate,
                                  enable_visualization)

            arr[j] = temp
            iteration += 1

            # Визуализируем процесс вставки
            visualize_sorting(arr, f"Итерация {iteration}: вставка элемента {temp}", iteration, update_rate,
                              enable_visualization)

        gap //= 2  # Уменьшаем разрыв

    logging.info(f"Конечный отсортированный массив: {arr}")

    # Финальная визуализация после завершения сортировки
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1,
                      enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None

    return arr
