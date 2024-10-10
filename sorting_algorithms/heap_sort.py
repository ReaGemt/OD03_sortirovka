from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt


def heap_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация пирамидальной сортировки (Heap Sort) с возможностью включения/выключения визуализации
    и контролем частоты обновления графиков.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    n = len(arr)
    plt.ion() if enable_visualization else None
    iteration = 0  # Счётчик итераций

    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, iteration, enable_visualization, update_rate)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень в конец
        arr[i], arr[0] = arr[0], arr[i]
        logging.debug(f"Перемещение элемента {arr[i]} в конец массива")
        iteration += 1

        # Визуализация после каждого перемещения элемента
        visualize_sorting(arr, f"Итерация {iteration}: перемещение корня", iteration, update_rate, enable_visualization)

        # Вызываем heapify на уменьшенной куче
        heapify(arr, i, 0, iteration, enable_visualization, update_rate)

    logging.info(f"Конечный отсортированный массив: {arr}")

    # Финальная визуализация после завершения сортировки
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1,
                      enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None

    return arr


def heapify(arr, n, i, iteration, enable_visualization=True, update_rate=10):
    """
    Функция для преобразования поддерева с корнем в элементе i в кучу.

    Parameters:
    - arr: массив
    - n: размер кучи
    - i: индекс корня поддерева
    - iteration: текущая итерация для визуализации
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления визуализации
    """
    largest = i  # Инициализация наибольшего элемента как корня
    left = 2 * i + 1  # Левый дочерний элемент
    right = 2 * i + 2  # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше наибольшего элемента
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        logging.debug(f"Обмен элементов: {arr[i]} и {arr[largest]}")

        # Визуализация после каждого обмена
        iteration += 1
        visualize_sorting(arr, f"Итерация {iteration}: heapify", iteration, update_rate, enable_visualization)

        # Рекурсивно преобразуем поддерево в кучу
        heapify(arr, n, largest, iteration, enable_visualization, update_rate)
