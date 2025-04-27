class Methode:
    def __init__(self, type_methode: str):
        self.type_methode = type_methode

    def integrer(self, f, t, N, dt, env):
        if self.type_methode == "Euler":
            return N + dt * f(t, N, env)
        elif self.type_methode == "Runge-Kutta":
            k1 = f(t, N, env)
            k2 = f(t + dt/2, N + dt/2 * k1, env)
            k3 = f(t + dt/2, N + dt/2 * k2, env)
            k4 = f(t + dt, N + dt * k3, env)
            return N + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
        else:
            raise ValueError("Méthode inconnue")
