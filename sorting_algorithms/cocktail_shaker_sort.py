from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def cocktail_shaker_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация шейкерной сортировки (Cocktail Shaker Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    iteration = 0  # Счётчик для итераций

    plt.ion() if enable_visualization else None

    while swapped:
        swapped = False

        # Проход слева направо (как в обычной пузырьковой сортировке)
        for i in range(start, end):
            iteration += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                logging.debug(f"Обмен элементов {arr[i]} и {arr[i + 1]}")

            # Визуализируем процесс после каждого обмена
            visualize_sorting(arr, f"Итерация {iteration}: проход слева направо", iteration, update_rate,
                              enable_visualization)

        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

        # Уменьшаем конец, так как последний элемент уже на своём месте
        end -= 1
        swapped = False

        # Проход справа налево (обратный проход)
        for i in range(end - 1, start - 1, -1):
            iteration += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                logging.debug(f"Обмен элементов {arr[i]} и {arr[i + 1]}")

            # Визуализируем процесс после каждого обмена
            visualize_sorting(arr, f"Итерация {iteration}: проход справа налево", iteration, update_rate,
                              enable_visualization)

        # Увеличиваем начало, так как первый элемент уже на своём месте
        start += 1

    logging.info(f"Конечный отсортированный массив: {arr}")

    # Финальная визуализация после завершения сортировки
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1,
                      enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None

    return arr
