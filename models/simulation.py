from models.population import Population
from models.modele import Modele
from models.methode import Methode
from models.environnement import Environnement

class Simulation:
    def __init__(self, population: Population, modele: Modele, methode: Methode, environnement: Environnement, dt: float, duree: int):
        self.population = population
        self.modele = modele
        self.methode = methode
        self.environnement = environnement
        self.dt = dt
        self.duree = duree
        self.resultats = []

    def run(self):
        t = 0
        N = self.population.initial_count
        self.population.reset()
        self.resultats.append((t, N))

        while t < self.duree:
            N = self.methode.integrer(self.modele.croissance, t, N, self.dt, self.environnement)
            t += self.dt
            self.population.update(N)
            self.resultats.append((t, N))
