class Stadion:
    def __init__(self, sor):
        self.stadion = sor[0]
        self.varos = sor[1]
        self.csapatszam = int(sor[2])
        self.elso_merkozes = sor[3]
        self.utolso_merkozes = sor[4]


    def __str__(self, sor):
        return f"{self.stadion},{self.varos},{self.csapatszam},{self.elso_merkozes},{self.utolso_merkozes}"