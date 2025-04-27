import tkinter.messagebox as messagebox
from models.population import Population
from models.modele import Modele
from models.methode import Methode
from models.environnement import Environnement
from models.simulation import Simulation
from models.resultat import Resultat

class SimulationController:
    def __init__(self, view):
        self.view = view
        self.simulation = None

    def lancer_simulation(self):
        try:
            population = int(self.view.population_entry.get())
            growth = float(self.view.growth_entry.get()) / 100
            duree = int(self.view.duration_entry.get())
            pas = float(self.view.step_entry.get())
            resources = float(self.view.resources_entry.get()) / 100
            pollution = float(self.view.pollution_entry.get()) / 100
            temp = tuple(map(int, self.view.temp_entry.get().split("-")))
            modele = self.view.model_combobox.get()
            methode = self.view.method_combobox.get()

            pop = Population(population)
            mod = Modele(modele)
            meth = Methode(methode)
            env = Environnement(resources, pollution, temp)

            self.simulation = Simulation(pop, mod, meth, env, pas, duree)
            self.simulation.run()

            self.afficher_resultats(self.simulation.resultats)
            # Notifie le dashboard si la méthode existe
            if hasattr(self.view, "notify_dashboard"):
                self.view.notify_dashboard(self.simulation.resultats)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def afficher_resultats(self, resultats):
        self.view.ax.clear()
        t, N = zip(*resultats)
        self.view.ax.plot(t, N, label="Population simulée")
        self.view.ax.legend()
        self.view.canvas.draw()

        for row in self.view.tree.get_children():
            self.view.tree.delete(row)
        for t_val, n_val in resultats:
            self.view.tree.insert("", "end", values=(round(t_val,2), int(n_val)))

    def stop_simulation(self):
        messagebox.showinfo("Stop", "La simulation est arrêtée (fonctionnalité étendue plus tard).")

    def reset_simulation(self):
        self.view.population_entry.delete(0, "end")
        self.view.population_entry.insert(0, "10000")
        self.view.growth_entry.delete(0, "end")
        self.view.growth_entry.insert(0, "3")
        self.view.duration_entry.delete(0, "end")
        self.view.duration_entry.insert(0, "100")
        self.view.step_entry.delete(0, "end")
        self.view.step_entry.insert(0, "1")
        self.view.resources_entry.delete(0, "end")
        self.view.resources_entry.insert(0, "60")
        self.view.pollution_entry.delete(0, "end")
        self.view.pollution_entry.insert(0, "13")
        self.view.temp_entry.delete(0, "end")
        self.view.temp_entry.insert(0, "10-23")

    def exporter_resultats(self):
        import csv
        if not self.simulation:
            messagebox.showerror("Erreur", "Aucune simulation à exporter.")
            return
        with open("export_simulation.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Temps", "Population"])
            for t, n in self.simulation.resultats:
                writer.writerow([round(t, 2), int(n)])
        messagebox.showinfo("Export", "Exportation réussie vers 'export_simulation.csv'.")
