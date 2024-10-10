from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def merge_sort(arr, iteration=0, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки слиянием с возможностью включения/выключения визуализации
    и контролем частоты обновления графиков.

    Parameters:
    - arr: массив для сортировки
    - iteration: текущая итерация для визуализации
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    # Включаем интерактивный режим matplotlib
    plt.ion() if enable_visualization else None

    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Левая половина
        right_half = arr[mid:]  # Правая половина

        # Рекурсивно сортируем обе половины
        iteration = merge_sort(left_half, iteration, enable_visualization, update_rate)
        iteration = merge_sort(right_half, iteration, enable_visualization, update_rate)

        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            iteration += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

            # Визуализируем процесс слияния
            visualize_sorting(arr, f"Итерация {iteration}: слияние", iteration, update_rate, enable_visualization)

        # Добавляем оставшиеся элементы левой половины (если есть)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            iteration += 1
            visualize_sorting(arr, f"Итерация {iteration}: добавление левого", iteration, update_rate,
                              enable_visualization)

        # Добавляем оставшиеся элементы правой половины (если есть)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            iteration += 1
            visualize_sorting(arr, f"Итерация {iteration}: добавление правого", iteration, update_rate,
                              enable_visualization)

    logging.info(f"Конечный отсортированный массив: {arr}")

    return iteration


# Финализация визуализации
def finalize_visualization(enable_visualization=True):
    if enable_visualization:
        plt.show(block=True)
