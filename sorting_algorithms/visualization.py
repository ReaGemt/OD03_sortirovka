# sorting_algorithms/visualization.py
import time
import matplotlib.pyplot as plt
import logging

# Настройка логирования с форматированием
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def visualize_sorting(arr, title):
    """
    Визуализация текущего состояния сортировки с использованием столбчатой диаграммы.

    Parameters:
    - arr: текущий массив для отображения
    - title: заголовок для графика, описывающий текущий шаг сортировки
    """
    plt.clf()  # Очищаем предыдущий график
    plt.bar(range(len(arr)), arr, color="blue")  # Столбчатая диаграмма
    plt.title(title)  # Заголовок графика
    plt.pause(0.1)  # Пауза для отображения графика (0.1 секунд)
