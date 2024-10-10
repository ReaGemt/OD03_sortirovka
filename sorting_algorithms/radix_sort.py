# sorting_algorithms/radix_sort.py
from matplotlib import pyplot as plt
from visualization import visualize_sorting
import logging

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        visualize_sorting(count, f"Подсчёт для разряда {exp}")

    for i in range(1, 10):
        count[i] += count[i - 1]
        visualize_sorting(count, f"Модификация счётчика для разряда {exp}")

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
        visualize_sorting(arr, f"Построение выходного массива для разряда {exp}")

def radix_sort(arr):
    logging.info(f"Начальный массив: {arr}")
    max_val = max(arr)
    exp = 1
    plt.ion()
    fig = plt.figure()

    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        visualize_sorting(arr, f"Сортировка по разряду {exp}")
        exp *= 10

    visualize_sorting(arr, "Конечный отсортированный массив")
    plt.show(block=True)
    return arr
