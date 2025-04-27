class Resultat:
    def __init__(self, donnees: list):
        self.donnees = donnees

    def to_table(self):
        return [{"Temps": round(t, 2), "Population": int(N)} for t, N in self.donnees]
