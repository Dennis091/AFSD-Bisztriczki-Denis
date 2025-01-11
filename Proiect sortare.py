class SortingVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Algoritmi de Sortare Vizualizați")

        # Setări de bază
        self.num_elements = 50
        self.speed = 0.05  # Viteza animației
        self.array = [random.randint(10, 100) for _ in range(self.num_elements)]
        self.algorithm = "Bubble Sort"
        self.is_running = False
        self.is_paused = False

        # Configurăm UI-ul
        self.create_widgets()

    def create_widgets(self):
        """Crează interfața cu utilizatorul."""
        # Setarea Canvas pentru plot
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=4)
        self.ax.bar(range(len(self.array)), self.array, color='blue')

        # Setarea butoanelor
        self.start_button = tk.Button(self.master, text="Start", command=self.start_sorting)
        self.start_button.grid(row=1, column=0)
        
        self.pause_button = tk.Button(self.master, text="Pauză", command=self.pause_sorting)
        self.pause_button.grid(row=1, column=1)

        self.resume_button = tk.Button(self.master, text="Continuă", command=self.resume_sorting)
        self.resume_button.grid(row=1, column=2)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_array)
        self.reset_button.grid(row=1, column=3)

        # Selectorul de algoritmi
        self.algorithm_label = tk.Label(self.master, text="Selectează algoritmul:")
        self.algorithm_label.grid(row=2, column=0)
        
        self.algorithm_selector = tk.OptionMenu(self.master, tk.StringVar(value=self.algorithm), "Bubble Sort", "Insertion Sort", "Selection Sort", "Bogo Sort", command=self.change_algorithm)
        self.algorithm_selector.grid(row=2, column=1)

        # Selectorul de număr de elemente
        self.num_elements_label = tk.Label(self.master, text="Număr de elemente:")
        self.num_elements_label.grid(row=2, column=2)
        
        self.num_elements_slider = tk.Scale(self.master, from_=5, to=100, orient="horizontal", command=self.update_num_elements)
        self.num_elements_slider.set(self.num_elements)
        self.num_elements_slider.grid(row=2, column=3)

        # Selector de viteză
        self.speed_label = tk.Label(self.master, text="Viteza animației:")
        self.speed_label.grid(row=3, column=0)

        self.speed_slider = tk.Scale(self.master, from_=0.01, to=0.2, orient="horizontal", resolution=0.01, command=self.update_speed)
        self.speed_slider.set(self.speed)
        self.speed_slider.grid(row=3, column=1, columnspan=2)

        # Buton pentru a închide aplicația
        self.exit_button = tk.Button(self.master, text="Ieșire", command=self.master.quit)
        self.exit_button.grid(row=4, column=1)

    def update_num_elements(self, val):
        """Actualizează numărul de elemente."""
        self.num_elements = int(val)
        self.reset_array()

    def update_speed(self, val):
        """Actualizează viteza animației."""
        self.speed = float(val)

    def change_algorithm(self, algo):
        """Schimbă algoritmul de sortare selectat."""
        self.algorithm = algo

    def reset_array(self):
        """Resetează lista de elemente."""
        self.array = [random.randint(10, 100) for _ in range(self.num_elements)]
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='blue')
        self.canvas.draw()

    def start_sorting(self):
        """Pornește sortarea într-un thread separat."""
        if self.is_running:
            messagebox.showinfo("Informație", "Sortarea este deja în curs.")
            return
        self.is_running = True
        self.sorting_thread = threading.Thread(target=self.sort)
        self.sorting_thread.start()

    def pause_sorting(self):
        """Pune sortarea pe pauză."""
        self.is_paused = True

    def resume_sorting(self):
        """Continuă sortarea după pauză."""
        self.is_paused = False

    def sort(self):
        """Sortarea efectivă pe baza algoritmului selectat."""
        if self.algorithm == "Bubble Sort":
            self.bubble_sort()
        elif self.algorithm == "Insertion Sort":
            self.insertion_sort()
        elif self.algorithm == "Selection Sort":
            self.selection_sort()
        elif self.algorithm == "Bogo Sort":
            self.bogo_sort()

        self.is_running = False

    def bubble_sort(self):
        """Algoritmul Bubble Sort cu animație."""
        for i in range(len(self.array) - 1):
            if self.is_paused:
                while self.is_paused:
                    time.sleep(0.1)
            for j in range(len(self.array) - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                self.update_plot()
                time.sleep(self.speed)

    def insertion_sort(self):
        """Algoritmul Insertion Sort cu animație."""
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.update_plot()
            time.sleep(self.speed)

    def selection_sort(self):
        """Algoritmul Selection Sort cu animație."""
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_plot()
            time.sleep(self.speed)

    def bogo_sort(self):
        """Algoritmul Bogo Sort cu animație (ineficient)."""
        while not self.is_sorted():
            random.shuffle(self.array)
            self.update_plot()
            time.sleep(self.speed)

    def is_sorted(self):
        """Verifică dacă lista este sortată."""
        return all(self.array[i] <= self.array[i + 1] for i in range(len(self.array) - 1))

    def update_plot(self):
        """Actualizează grafica după fiecare pas."""
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='blue')
        self.canvas.draw()
