# sorting_algorithms/visualization.py
import matplotlib.pyplot as plt


def visualize_sorting(arr, title, iteration=0, update_rate=10, enable_visualization=True):
    """
    Визуализация текущего состояния сортировки с использованием столбчатой диаграммы.

    Parameters:
    - arr: текущий массив для отображения
    - title: заголовок для графика, описывающий текущий шаг сортировки
    - iteration: текущая итерация сортировки (для контроля частоты обновления)
    - update_rate: частота обновления визуализации (обновление каждые N итераций)
    - enable_visualization: включение/выключение визуализации
    """
    if not enable_visualization:
        return  # Если визуализация отключена, выходим из функции

    # Обновляем график только на каждой N-й итерации
    if iteration % update_rate == 0:
        plt.clf()  # Очищаем предыдущий график
        plt.bar(range(len(arr)), arr, color="blue")  # Столбчатая диаграмма
        plt.title(title)  # Заголовок графика
        plt.draw()  # Принудительно отрисовываем график
        plt.pause(0.01)  # Короткая пауза для обновления (0.01 секунд)
