import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from models.statistique import Statistique

class DashboardView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F5F5F5")

        # Titre stylisé
        title = tk.Label(self, text="Dashboard", font=("Segoe UI", 22, "bold"), bg="#F5F5F5", fg="#2C3E50")
        title.pack(pady=20)

        # Résumés
        self.stats_frame = tk.Frame(self, bg="#F5F5F5")
        self.stats_frame.pack()

        label_style = {"font": ("Segoe UI", 14), "bg": "#F5F5F5", "fg": "#34495E"}
        self.nb_sim_label = tk.Label(self.stats_frame, text="Nombre de simulations : 0", **label_style)
        self.nb_sim_label.grid(row=0, column=0, padx=20, pady=10)

        self.last_sim_label = tk.Label(self.stats_frame, text="Dernier modèle : -", **label_style)
        self.last_sim_label.grid(row=0, column=1, padx=20, pady=10)

        self.percentage_label = tk.Label(self.stats_frame, text="Pourcentage d'imp/exp : 0 / 0", **label_style)
        self.percentage_label.grid(row=0, column=2, padx=20, pady=10)

        # Graphique + Table
        self.graph_frame = tk.Frame(self, bg="#F5F5F5")
        self.graph_frame.pack(pady=20)

        self.figure = plt.figure(figsize=(6,4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.chart = FigureCanvasTkAgg(self.figure, self.graph_frame)
        self.chart.get_tk_widget().pack(side=tk.LEFT)

        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="#F5F5F5", fieldbackground="#F5F5F5")
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#34495E", foreground="white")

        self.tree = ttk.Treeview(self.graph_frame, columns=("Temps", "Population"), show="headings", style="Treeview")
        self.tree.heading("Temps", text="Temps")
        self.tree.heading("Population", text="Population")
        self.tree.pack(side=tk.RIGHT, padx=20, fill="y", expand=True)

    def update_dashboard(self, data, simulation_count, last_modele, import_percent, export_percent):
        # Statistiques
        self.nb_sim_label.config(text=f"Nombre de simulations : {simulation_count}")
        self.last_sim_label.config(text=f"Dernier modèle : {last_modele}")
        self.percentage_label.config(text=f"Pourcentage d'imp/exp : {import_percent:.3f} / {export_percent:.3f}")

        # Graphique
        self.ax.clear()
        if data:
            t, N = zip(*data)
            self.ax.plot(t, N, color="purple", label="Population")
            self.ax.set_title("Simulation récente")
            self.ax.set_xlabel("Temps")
            self.ax.set_ylabel("Population")
            self.ax.legend()
        self.chart.draw()

        # Table
        for row in self.tree.get_children():
            self.tree.delete(row)
        for t_val, n_val in data:
            self.tree.insert("", "end", values=(round(t_val,2), int(n_val)))
