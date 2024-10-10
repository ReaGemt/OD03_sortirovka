import matplotlib.pyplot as plt


def visualize_sorting(arr, title, iteration=0, update_rate=10, enable_visualization=True):
    """
    Функция для визуализации текущего состояния массива при сортировке.

    Parameters:
    - arr: массив для сортировки
    - title: заголовок графика
    - iteration: текущая итерация сортировки (для управления частотой обновления)
    - update_rate: частота обновления графика (график обновляется каждые N итераций)
    - enable_visualization: флаг включения визуализации
    """
    if not enable_visualization:
        return  # Если визуализация отключена, не выполняем обновление

    # Обновляем график каждые N итераций
    if iteration % update_rate == 0:
        plt.clf()  # Очистка текущего графика
        plt.bar(range(len(arr)), arr, color='blue')  # Построение столбчатой диаграммы
        plt.title(title)  # Установка заголовка
        plt.pause(0.01)  # Короткая пауза для обновления графика


def finalize_visualization(enable_visualization=True):
    """
    Финализирующая функция для отображения графика после завершения сортировки.

    Parameters:
    - enable_visualization: флаг включения визуализации
    """
    if enable_visualization:
        plt.show(block=True)  # Отображение финального графика и блокировка до закрытия окна

    plt.close()  # Закрытие графика