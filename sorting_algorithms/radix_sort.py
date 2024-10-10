from visualization import visualize_sorting
import logging
import matplotlib.pyplot as plt

def counting_sort_for_radix(arr, exp, iteration, enable_visualization=True, update_rate=10):
    """
    Вспомогательная функция для сортировки по текущему разряду с использованием
    сортировки подсчётом для поразрядной сортировки.

    Parameters:
    - arr: массив для сортировки
    - exp: текущий разряд
    - iteration: текущая итерация для визуализации
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Инициализация подсчета для цифр от 0 до 9

    # Подсчитываем количество вхождений для каждого числа в текущем разряде
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        iteration += 1
        # Визуализируем процесс подсчёта
        visualize_sorting(count, f"Итерация {iteration}: подсчёт для разряда {exp}", iteration, update_rate, enable_visualization)

    # Модифицируем count, чтобы хранить позиции элементов
    for i in range(1, 10):
        count[i] += count[i - 1]
        iteration += 1
        # Визуализируем процесс модификации счётчика
        visualize_sorting(count, f"Итерация {iteration}: модификация счётчика для разряда {exp}", iteration, update_rate, enable_visualization)

    # Строим выходной массив
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        iteration += 1
        # Визуализируем процесс построения выходного массива
        visualize_sorting(output, f"Итерация {iteration}: построение выходного массива для разряда {exp}", iteration, update_rate, enable_visualization)

    # Копируем отсортированный массив обратно в arr
    for i in range(n):
        arr[i] = output[i]

    return iteration


def radix_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация поразрядной сортировки (Radix Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    # Находим максимальное значение для определения количества разрядов
    max_val = max(arr)
    exp = 1  # Начинаем с младшего разряда (единицы)
    iteration = 0  # Для отслеживания итераций

    plt.ion() if enable_visualization else None

    # Выполняем сортировку для каждого разряда
    while max_val // exp > 0:
        iteration = counting_sort_for_radix(arr, exp, iteration, enable_visualization, update_rate)
        exp *= 10  # Переходим к следующему разряду

    logging.info(f"Конечный отсортированный массив: {arr}")

    # Финальная визуализация после завершения сортировки
    visualize_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None

    return arr
