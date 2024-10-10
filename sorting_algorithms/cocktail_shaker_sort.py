# sorting_algorithms/shell_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging


def shell_sort(arr):
    """
    Реализация сортировки Шелла с визуализацией и логированием.

    Алгоритм сортирует элементы массива по возрастанию, используя промежутки (gap),
    которые постепенно уменьшаются. Это улучшенная версия сортировки вставками.

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    # Инициализируем начальный разрыв (gap), который равен половине длины массива
    gap = n // 2

    plt.ion()  # Включаем интерактивный режим для визуализации
    fig = plt.figure()

    # Цикл продолжается до тех пор, пока разрыв (gap) больше нуля
    while gap > 0:
        logging.debug(f"Текущий разрыв (gap): {gap}")

        # Проходим по всем элементам массива, начиная с элемента, стоящего после разрыва
        for i in range(gap, n):
            temp = arr[i]  # Сохраняем текущий элемент для дальнейшей вставки
            j = i

            # Выполняем сдвиг элементов, если они больше текущего temp
            while j >= gap and arr[j - gap] > temp:
                logging.debug(f"Сдвигаем {arr[j - gap]} на позицию {j}")
                arr[j] = arr[j - gap]
                j -= gap  # Сдвигаем указатель на gap позиций назад

            # Вставляем текущий элемент (temp) на его правильное место
            arr[j] = temp
            logging.debug(f"Вставляем элемент {temp} на позицию {j}")
            visualize_sorting(arr, f"Текущий разрыв {gap}. Вставка элемента {temp}")

        # Уменьшаем разрыв (gap) в два раза
        gap //= 2
        logging.debug(f"Уменьшение разрыва. Новый разрыв (gap): {gap}")
        visualize_sorting(arr, f"Уменьшение разрыва до {gap}")

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)  # Оставляем график на экране
    return arr
