# sorting_algorithms/radix_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def counting_sort_for_radix(arr, exp):
    """
    Вспомогательная функция для выполнения сортировки подсчётом для конкретного разряда.

    Parameters:
    - arr: массив для сортировки
    - exp: текущий разряд (единицы, десятки, сотни и т.д.)

    Returns:
    - Отсортированный массив по текущему разряду
    """
    n = len(arr)
    output = [0] * n  # Массив для хранения отсортированных по разряду элементов
    count = [0] * 10  # Массив для подсчёта количества цифр

    logging.debug(f"Подсчёт количества элементов для разряда {exp}...")

    # Подсчёт количества каждой цифры в текущем разряде
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        visualize_sorting(count, f"Подсчёт для разряда {exp}, цифра {index}")

    # Модификация count для хранения конечных позиций цифр
    logging.debug(f"Модификация счётчика для позиций по разряду {exp}...")
    for i in range(1, 10):
        count[i] += count[i - 1]
        visualize_sorting(count, f"Обновление позиции для цифры {i}")

    # Построение выходного массива на основе count
    logging.debug(f"Построение отсортированного массива для разряда {exp}...")
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        visualize_sorting(output, f"Построение массива по разряду {exp}, элемент {arr[i]}")

    # Копируем отсортированные элементы обратно в оригинальный массив
    for i in range(n):
        arr[i] = output[i]
        visualize_sorting(arr, f"Копирование отсортированных элементов для разряда {exp}")

def radix_sort(arr):
    """
    Реализация поразрядной сортировки с логированием и визуализацией.

    Алгоритм сортирует числа по разрядам (единицы, десятки, сотни и т.д.).

    Parameters:
    - arr: массив для сортировки

    Returns:
    - Отсортированный массив
    """
    logging.info(f"Начальный массив: {arr}")

    # Находим максимальный элемент для определения количества разрядов
    max_val = max(arr)
    exp = 1  # Начинаем с единиц (exp = 1)

    plt.ion()
    fig = plt.figure()

    # Сортировка по каждому разряду, начиная с единиц
    while max_val // exp > 0:
        logging.debug(f"Сортировка по разряду {exp}...")
        counting_sort_for_radix(arr, exp)
        visualize_sorting(arr, f"Сортировка по разряду {exp}")
        exp *= 10  # Переходим к следующему разряду (десятки, сотни и т.д.)

    logging.info(f"Конечный отсортированный массив: {arr}")
    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
