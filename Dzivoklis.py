class Dzivoklis:
    def __init__(self, link, iela, istabuSkaits, laukumsM2, stāvs, sērija, cenaM2, cena):
        self.link = link
        self.iela = iela
        self.istabuSkaits = istabuSkaits
        self.laukumsM2 = laukumsM2
        self.stāvs = stāvs
        self.sērija = sērija
        self.cenaM2 = cenaM2
        self.cena = cena
    def DZIVprint(self):
        print(
            f"Link: {self.link}, "
            f"Iela: {self.iela}, "
            f"Istabu skaits: {self.istabuSkaits}, "
            f"Laukums (m2): {self.laukumsM2}, "
            f"Stāvs: {self.stāvs}, "
            f"Sērija: {self.sērija}, "
            f"Cena/m2: {self.cenaM2}, "
            f"Cena: {self.cena}"
        )
    def DzivAllDataGetter(self):
        return [
            self.link,
            self.iela,
            self.istabuSkaits,
            self.laukumsM2,
            self.stāvs,
            self.sērija,
            self.cenaM2,
            self.cena
        ]