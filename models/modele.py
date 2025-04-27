import numpy as np

class Modele:
    def __init__(self, type_modele: str):
        self.type_modele = type_modele

    def croissance(self, t, N, env):
        if self.type_modele == "Malthus":
            return 0.03 * N
        elif self.type_modele == "Verhulst":
            return 0.03 * N * (1 - N / (env.resources * 10000))
        elif self.type_modele == "Hyperbolique":
            return 0.03 * N**2
        elif self.type_modele == "Log-logistique":
            return 0.03 * N * (1 - (N / (env.resources * 10000))**2)
        elif self.type_modele == "Gompertz":
            return 0.03 * N * (1 - np.log(N) / np.log(env.resources * 10000))
        else:
            raise ValueError("Modèle inconnu")
