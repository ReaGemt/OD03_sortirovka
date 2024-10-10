from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt
import time


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

    # Замер времени начала сортировки
    start_time = time.time()

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

    # Замер времени окончания сортировки
    end_time = time.time()
    total_time = end_time - start_time  # Вычисляем общее время выполнения сортировки

    logging.info(f"Конечный отсортированный массив: {arr}")
    logging.info(f"Время выполнения: {total_time:.4f} секунд")

    # Финальная визуализация после завершения сортировки с добавлением времени выполнения
    if enable_visualization:
        plt.clf()  # Очищаем график перед финальной визуализацией
        plt.bar(range(len(arr)), arr, color='blue')  # Отображаем финальный отсортированный массив
        plt.title(f"Конечный отсортированный массив\nВремя выполнения: {total_time:.4f} секунд")
        plt.draw()
        plt.show(block=True)

    return arr
