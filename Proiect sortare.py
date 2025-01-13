import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Algoritmii de sortare
def bubble_sort(arr, canvas, speed=0.1):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            update_canvas(arr, canvas)
            time.sleep(speed)

def insertion_sort(arr, canvas, speed=0.1):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        update_canvas(arr, canvas)
        time.sleep(speed)

def selection_sort(arr, canvas, speed=0.1):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_canvas(arr, canvas)
        time.sleep(speed)

def bogo_sort(arr, canvas, speed=0.1):
    while not is_sorted(arr):
        random.shuffle(arr)
        update_canvas(arr, canvas)
        time.sleep(speed)

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Actualizarea canvas-ului
def update_canvas(arr, canvas):
    canvas.cla()  # Clear current plot
    canvas.bar(range(len(arr)), arr, color="blue")
    canvas.set_title("Sorting Animation")
    canvas.set_ylabel("Value")
    canvas.set_xlabel("Index")
    canvas.figure.canvas.draw()

# Setarea vizualizării și interfața
class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        
        self.num_elements = 50
        self.speed = 0.1
        self.array = [random.randint(10, 100) for _ in range(self.num_elements)]
        
        self.create_widgets()
        self.create_plot()
    
    def create_widgets(self):
        # Selector de algoritmi
        self.algorithm_label = tk.Label(self.root, text="Select Algorithm:")
        self.algorithm_label.grid(row=0, column=0)
        
        self.algorithm_combo = ttk.Combobox(self.root, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Bogo Sort"])
        self.algorithm_combo.set("Bubble Sort")
        self.algorithm_combo.grid(row=0, column=1)
        
        # Viteza animației
        self.speed_label = tk.Label(self.root, text="Speed:")
        self.speed_label.grid(row=1, column=0)
        
        self.speed_scale = tk.Scale(self.root, from_=0.01, to=1, resolution=0.01, orient="horizontal")
        self.speed_scale.set(self.speed)
        self.speed_scale.grid(row=1, column=1)
        
        # Buton pentru randomizare
        self.randomize_button = tk.Button(self.root, text="Randomize", command=self.randomize)
        self.randomize_button.grid(row=2, column=0, columnspan=2)
        
        # Buton de start
        self.start_button = tk.Button(self.root, text="Start", command=self.start_sorting)
        self.start_button.grid(row=3, column=0)
        
        # Buton de reset
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=1)
    
    def create_plot(self):
        # Crearea figurei pentru vizualizarea animației
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.ax.set_title("Sorting Animation")
        self.ax.set_ylabel("Value")
        self.ax.set_xlabel("Index")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)
    
    def randomize(self):
        self.array = [random.randint(10, 100) for _ in range(self.num_elements)]
        self.update_plot()
    
    def start_sorting(self):
        algorithm = self.algorithm_combo.get()
        speed = self.speed_scale.get()
        
        if algorithm == "Bubble Sort":
            threading.Thread(target=bubble_sort, args=(self.array, self.ax, speed)).start()
        elif algorithm == "Insertion Sort":
            threading.Thread(target=insertion_sort, args=(self.array, self.ax, speed)).start()
        elif algorithm == "Selection Sort":
            threading.Thread(target=selection_sort, args=(self.array, self.ax, speed)).start()
        elif algorithm == "Bogo Sort":
            threading.Thread(target=bogo_sort, args=(self.array, self.ax, speed)).start()
    
    def reset(self):
        self.array = [random.randint(10, 100) for _ in range(self.num_elements)]
        self.update_plot()
    
    def update_plot(self):
        self.ax.cla()
        self.ax.bar(range(len(self.array)), self.array, color="blue")
        self.ax.set_title("Sorting Animation")
        self.ax.set_ylabel("Value")
        self.ax.set_xlabel("Index")
        self.canvas.draw()

# Crearea aplicației
def main():
    root = tk.Tk()
    app = SortVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
