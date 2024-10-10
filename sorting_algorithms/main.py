import tkinter as tk
from tkinter import ttk
import logging
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort, finalize_visualization
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort
from cocktail_shaker_sort import cocktail_shaker_sort
from shell_sort import shell_sort

# Массивы для тестирования
arrays = {
    "Bubble Sort": [64, 34, 25, 12, 22, 11, 90],
    "Selection Sort": [64, 25, 12, 22, 11],
    "Quick Sort": [3, 6, 8, 10, 1, 2, 1],
    "Insertion Sort": [12, 11, 13, 5, 6],
    "Merge Sort": [12, 11, 13, 5, 6, 7],
    "Heap Sort": [12, 11, 13, 5, 6, 7],
    "Counting Sort": [4, 2, 2, 8, 3, 3, 1],
    "Radix Sort": [170, 45, 75, 90, 802, 24, 2, 66],
    "Cocktail Shaker Sort": [5, 1, 4, 2, 8, 0, 2],
    "Shell Sort": [12, 34, 54, 2, 3],
}

# Функция для настройки уровня логирования
def set_logging_level(level):
    logging.getLogger().setLevel(level)
    logging.info(f"Уровень логирования установлен на: {logging.getLevelName(level)}")

# Функция для запуска выбранного алгоритма
def run_selected_sort():
    selected_algorithm = algorithm_var.get()
    enable_visualization = visualization_var.get()
    update_rate = int(update_rate_var.get())

    logging.info(f"Запуск {selected_algorithm} с визуализацией={enable_visualization} и update_rate={update_rate}")

    array = arrays[selected_algorithm].copy()

    # Выбираем и запускаем нужный алгоритм сортировки
    if selected_algorithm == "Bubble Sort":
        bubble_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Selection Sort":
        selection_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Quick Sort":
        quick_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Insertion Sort":
        insertion_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Merge Sort":
        merge_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Heap Sort":
        heap_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Counting Sort":
        counting_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Radix Sort":
        radix_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Cocktail Shaker Sort":
        cocktail_shaker_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Shell Sort":
        shell_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)

    # Окончательная визуализация для всех алгоритмов
    finalize_visualization(enable_visualization=enable_visualization)

# Создаем главное окно Tkinter
root = tk.Tk()
root.title("Sorting Algorithms")

# Выпадающий список для выбора алгоритма сортировки
algorithm_var = tk.StringVar()
algorithm_label = ttk.Label(root, text="Выберите алгоритм сортировки:")
algorithm_label.pack(pady=5)

algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var)
algorithm_menu['values'] = list(arrays.keys())
algorithm_menu.current(0)
algorithm_menu.pack(pady=5)

# Чекбокс для включения/выключения визуализации
visualization_var = tk.BooleanVar(value=True)
visualization_check = ttk.Checkbutton(root, text="Включить визуализацию", variable=visualization_var)
visualization_check.pack(pady=5)

# Поле для ввода частоты обновления графиков
update_rate_var = tk.StringVar(value="10")
update_rate_label = ttk.Label(root, text="Частота обновления графика (N итераций):")
update_rate_label.pack(pady=5)

update_rate_entry = ttk.Entry(root, textvariable=update_rate_var)
update_rate_entry.pack(pady=5)

# Выпадающий список для выбора уровня логирования
log_level_var = tk.StringVar()
log_level_label = ttk.Label(root, text="Выберите уровень логирования:")
log_level_label.pack(pady=5)

log_level_menu = ttk.Combobox(root, textvariable=log_level_var)
log_level_menu['values'] = ['DEBUG', 'INFO']
log_level_menu.current(1)  # INFO по умолчанию
log_level_menu.pack(pady=5)

# Кнопка для настройки уровня логирования
set_log_button = ttk.Button(root, text="Установить уровень логирования",
                            command=lambda: set_logging_level(getattr(logging, log_level_var.get())))
set_log_button.pack(pady=5)

# Кнопка для запуска сортировки
run_button = ttk.Button(root, text="Запустить сортировку", command=run_selected_sort)
run_button.pack(pady=20)

# Настройка логирования по умолчанию
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Запуск главного цикла Tkinter
root.mainloop()
