# sorting_algorithms/visualization.py
import time
import matplotlib.pyplot as plt
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

def visualize_sorting(arr, title):
    """
    Визуализация текущего состояния сортировки
    """
    plt.clf()  # Очищаем предыдущий график
    plt.bar(range(len(arr)), arr, color="blue")  # Создаем столбчатую диаграмму
    plt.title(title)  # Заголовок графика
    plt.pause(0.1)  # Пауза для отображения графика (0.1 секунд)
