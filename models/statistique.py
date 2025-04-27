class Statistique:
    @staticmethod
    def analyse(donnees: list):
        temps, populations = zip(*donnees)
        croissance = (populations[-1] - populations[0]) / populations[0]
        return {
            "Population Initiale": populations[0],
            "Population Finale": populations[-1],
            "Croissance Relative": croissance,
            "Durée": temps[-1]
        }
