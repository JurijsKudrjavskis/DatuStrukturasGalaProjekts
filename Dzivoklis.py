class Dzivoklis:
    def __init__(self, link, iela, istabuSkaits, laukumsM2, stavs, serija, cenaM2, cena):
        self.link = link
        self.iela = iela
        self.istabuSkaits = istabuSkaits
        self.laukumsM2 = laukumsM2
        self.stavs = stavs
        self.serija = serija
        self.cenaM2 = cenaM2
        self.cena = cena
    def DZIVprint(self):
        print(
            f"Link: {self.link}, "
            f"Iela: {self.iela}, "
            f"Istabu skaits: {self.istabuSkaits}, "
            f"Laukums (m2): {self.laukumsM2}, "
            f"Stāvs: {self.stavs}, "
            f"Sērija: {self.serija}, "
            f"Cena/m2: {self.cenaM2}, "
            f"Cena: {self.cena}"
        )
    def DzivAllDataGetter(self):
        return [
            self.link,
            self.iela,
            self.istabuSkaits,
            self.laukumsM2,
            self.stavs,
            self.serija,
            self.cenaM2,
            self.cena
        ]
    def get_link(self):
        return self.link

    def get_iela(self):
        return self.iela

    def get_istabu_skaits(self):
        return self.istabuSkaits

    def get_laukums_m2(self):
        return self.laukumsM2

    def get_stavs(self):
        return self.stavs

    def get_serija(self):
        return self.serija

    def get_cena_m2(self):
        return self.cenaM2

    def get_cena(self):
        return self.cena