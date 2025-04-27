import tkinter as tk
from tkinter import ttk
from controllers.simulation_controller import SimulationController

class SimulationView(tk.Frame):
    def __init__(self, parent, main_view):
        super().__init__(parent, bg="#F5F5F5")
        self.main_view = main_view

        self.controller = SimulationController(self)

        # Paramètres de simulation
        self.param_frame = tk.Frame(self, bg="#F5F5F5", bd=2, relief="groove")
        self.param_frame.pack(side="left", fill="y", padx=20, pady=20)

        label_style = {"bg": "#F5F5F5", "font": ("Segoe UI", 11)}
        entry_style = {"font": ("Segoe UI", 11), "bd": 2, "relief": "sunken"}

        tk.Label(self.param_frame, text="Nombre d'individus initiaux", **label_style).pack(pady=(10,0), anchor="w")
        self.population_entry = tk.Entry(self.param_frame, **entry_style)
        self.population_entry.insert(0, "10000")
        self.population_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Taux de croissance (%)", **label_style).pack(pady=(10,0), anchor="w")
        self.growth_entry = tk.Entry(self.param_frame, **entry_style)
        self.growth_entry.insert(0, "3")
        self.growth_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Durée de simulation", **label_style).pack(pady=(10,0), anchor="w")
        self.duration_entry = tk.Entry(self.param_frame, **entry_style)
        self.duration_entry.insert(0, "100")
        self.duration_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Pas de temps", **label_style).pack(pady=(10,0), anchor="w")
        self.step_entry = tk.Entry(self.param_frame, **entry_style)
        self.step_entry.insert(0, "1")
        self.step_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Ressources disponibles (%)", **label_style).pack(pady=(10,0), anchor="w")
        self.resources_entry = tk.Entry(self.param_frame, **entry_style)
        self.resources_entry.insert(0, "60")
        self.resources_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Taux de pollution (%)", **label_style).pack(pady=(10,0), anchor="w")
        self.pollution_entry = tk.Entry(self.param_frame, **entry_style)
        self.pollution_entry.insert(0, "13")
        self.pollution_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Température (min-max)", **label_style).pack(pady=(10,0), anchor="w")
        self.temp_entry = tk.Entry(self.param_frame, **entry_style)
        self.temp_entry.insert(0, "10-23")
        self.temp_entry.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Modèle", **label_style).pack(pady=(10,0), anchor="w")
        self.model_combobox = ttk.Combobox(self.param_frame, values=["Malthus", "Verhulst", "Hyperbolique", "Log-logistique", "Gompertz"], font=("Segoe UI", 11))
        self.model_combobox.set("Log-logistique")
        self.model_combobox.pack(fill="x", pady=2)

        tk.Label(self.param_frame, text="Méthode", **label_style).pack(pady=(10,0), anchor="w")
        self.method_combobox = ttk.Combobox(self.param_frame, values=["Runge-Kutta", "Euler"], font=("Segoe UI", 11))
        self.method_combobox.set("Runge-Kutta")
        self.method_combobox.pack(fill="x", pady=2)

        # Boutons stylisés
        self.button_frame = tk.Frame(self.param_frame, bg="#F5F5F5")
        self.button_frame.pack(pady=20)
        tk.Button(self.button_frame, text="Lancer", command=self.controller.lancer_simulation, bg="#27AE60", fg="white", font=("Segoe UI", 11), width=12).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Arrêter", command=self.controller.stop_simulation, bg="#C0392B", fg="white", font=("Segoe UI", 11), width=12).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Réinitialiser", command=self.controller.reset_simulation, bg="#2980B9", fg="white", font=("Segoe UI", 11), width=12).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.button_frame, text="Exporter", command=self.controller.exporter_resultats, bg="#7F8C8D", fg="white", font=("Segoe UI", 11), width=12).grid(row=1, column=1, padx=5, pady=5)

        # Zone de graphe et résultats
        self.output_frame = tk.Frame(self, bg="#F5F5F5")
        self.output_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        self.figure = None
        self.canvas = None
        self.tree = None
        self.setup_output()

    def setup_output(self):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        self.figure = plt.figure(figsize=(5,4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.output_frame)
        self.canvas.get_tk_widget().pack()

        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="#F5F5F5", fieldbackground="#F5F5F5")
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#34495E", foreground="white")

        self.tree = ttk.Treeview(self.output_frame, columns=("Temps", "Population"), show="headings", style="Treeview")
        self.tree.heading("Temps", text="Temps")
        self.tree.heading("Population", text="Population")
        self.tree.pack(fill="both", expand=True, pady=10)

    def notify_dashboard(self, resultats):
        modele = self.model_combobox.get()
        # Ici, tu peux calculer import_percent/export_percent si tu as la logique
        import_percent = 0
        export_percent = 0
        self.main_view.notify_simulation(resultats, modele, import_percent, export_percent)
