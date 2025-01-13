import tkinter as tk
from tkinter import ttk
import random
import time
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Sorting Algorithms
def bubble_sort(data, draw_data, delay):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            draw_data(data, ["red" if x == j or x == j+1 else "blue" for x in range(len(data))])
            time.sleep(delay)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ["green" if x == j or x == j+1 else "blue" for x in range(len(data))])
                time.sleep(delay)
    draw_data(data, ["green" for _ in range(len(data))])

def insertion_sort(data, draw_data, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            draw_data(data, ["red" if x == j or x == j+1 else "blue" for x in range(len(data))])
            time.sleep(delay)
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
        draw_data(data, ["green" if x <= i else "blue" for x in range(len(data))])
        time.sleep(delay)
    draw_data(data, ["green" for _ in range(len(data))])

def selection_sort(data, draw_data, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            draw_data(data, ["red" if x == j or x == min_idx else "blue" for x in range(len(data))])
            time.sleep(delay)
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ["green" if x <= i else "blue" for x in range(len(data))])
        time.sleep(delay)
    draw_data(data, ["green" for _ in range(len(data))])

# Helper Functions
def draw_data(data, color_array):
    canvas.clear()
    canvas.bar(range(len(data)), data, color=color_array)
    chart.draw()

def generate_data():
    global data
    data = [random.randint(1, 100) for _ in range(size_var.get())]
    draw_data(data, ["blue" for _ in range(len(data))])

def start_sorting():
    global data
    delay = speed_var.get()
    algo = algo_var.get()

    if algo == "Bubble Sort":
        threading.Thread(target=bubble_sort, args=(data, draw_data, delay)).start()
    elif algo == "Insertion Sort":
        threading.Thread(target=insertion_sort, args=(data, draw_data, delay)).start()
    elif algo == "Selection Sort":
        threading.Thread(target=selection_sort, args=(data, draw_data, delay)).start()

def reset():
    generate_data()

# Main Application
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("900x700")

# Variables
data = []
speed_var = tk.DoubleVar(value=0.1)
size_var = tk.IntVar(value=20)
algo_var = tk.StringVar(value="Bubble Sort")

# UI Elements
frame = ttk.Frame(root)
frame.pack(pady=10)

# Algorithm Selector
algo_label = ttk.Label(frame, text="Algorithm:")
algo_label.grid(row=0, column=0, padx=5, pady=5)
algo_menu = ttk.Combobox(frame, textvariable=algo_var, values=["Bubble Sort", "Insertion Sort", "Selection Sort"])
algo_menu.grid(row=0, column=1, padx=5, pady=5)

# Speed Control
speed_label = ttk.Label(frame, text="Speed:")
speed_label.grid(row=1, column=0, padx=5, pady=5)
speed_scale = ttk.Scale(frame, from_=0.01, to=1.0, orient="horizontal", variable=speed_var)
speed_scale.grid(row=1, column=1, padx=5, pady=5)

# Size Control
size_label = ttk.Label(frame, text="Size:")
size_label.grid(row=2, column=0, padx=5, pady=5)
size_scale = ttk.Scale(frame, from_=5, to=100, orient="horizontal", variable=size_var)
size_scale.grid(row=2, column=1, padx=5, pady=5)

# Buttons
generate_button = ttk.Button(frame, text="Generate", command=generate_data)
generate_button.grid(row=3, column=0, padx=5, pady=5)
start_button = ttk.Button(frame, text="Start", command=start_sorting)
start_button.grid(row=3, column=1, padx=5, pady=5)
reset_button = ttk.Button(frame, text="Reset", command=reset)
reset_button.grid(row=4, column=0, columnspan=2, pady=5)

# Visualization Area
fig = Figure(figsize=(8, 5), dpi=100)
canvas = fig.add_subplot(111)
chart = FigureCanvasTkAgg(fig, master=root)
chart.get_tk_widget().pack()

# Initialize
generate_data()

# Run Application
root.mainloop()
