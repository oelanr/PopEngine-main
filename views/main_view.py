import tkinter as tk
from views.dashboard_view import DashboardView
from views.simulation_view import SimulationView

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PopEngine")
        self.geometry("1200x700")
        self.configure(bg="#ECECEC")  # Couleur de fond générale

        # Barre de titre stylisée
        self.title_bar = tk.Label(self, text="PopEngine", font=("Segoe UI", 22, "bold"), bg="#2C3E50", fg="white", pady=10)
        self.title_bar.pack(side="top", fill="x")

        self.font = ("Segoe UI", 12)
        self.sidebar = tk.Frame(self, bg="#2C3E50", width=200)
        self.sidebar.pack(side="left", fill="y")

        self.main_area = tk.Frame(self, bg="#F5F5F5")
        self.main_area.pack(side="right", expand=True, fill="both")

        self.pages = {}
        self.simulation_history = []
        self.last_simulation_name = "-"
        self.last_simulation_date = "-"
        self.import_percent = 0
        self.export_percent = 0

        self.create_sidebar()
        self.show_dashboard()

    def create_sidebar(self):
        button_style = {
            "font": self.font,
            "bg": "#34495E",
            "fg": "white",
            "activebackground": "#1ABC9C",
            "bd": 0,
            "relief": "flat",
            "height": 2
        }
        tk.Button(self.sidebar, text="Dashboard", command=self.show_dashboard, **button_style).pack(pady=10, fill="x")
        tk.Button(self.sidebar, text="Nouvelle simulation", command=self.show_simulation, **button_style).pack(pady=10, fill="x")

    def show_dashboard(self):
        self.clear_main()
        self.pages["dashboard"] = DashboardView(self.main_area)
        self.pages["dashboard"].pack(fill="both", expand=True)
        # Mets à jour le dashboard sur la nouvelle instance
        self.pages["dashboard"].update_dashboard(
            self.simulation_history[-1] if self.simulation_history else [],
            len(self.simulation_history),
            self.last_simulation_name,
            self.import_percent,
            self.export_percent
        )

    def show_simulation(self):
        self.clear_main()
        # Passe une référence à MainView pour pouvoir notifier le dashboard
        self.pages["simulation"] = SimulationView(self.main_area, self)
        self.pages["simulation"].pack(fill="both", expand=True)

    def notify_simulation(self, resultats, modele, import_percent=0, export_percent=0):
        from datetime import datetime
        self.simulation_history.append(resultats)
        self.last_simulation_name = modele
        self.last_simulation_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.import_percent = import_percent
        self.export_percent = export_percent
        # Ne fais PAS de update_dashboard ici !

    def clear_main(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
