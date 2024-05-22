from datetime import datetime


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas_letrehozasa(self, szoba, datum):
        if datum < datetime.now():
            raise ValueError("A dátum nem lehet múltbéli.")

        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                raise ValueError("A szoba már foglalt ezen a napon.")

        uj_foglalas = Foglalas(szoba, datum)
        self.foglalasok.append(uj_foglalas)
        return szoba.get_ar()

    def foglalas_lemondasa(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        raise ValueError("Nincs ilyen foglalás.")

    def foglalasok_listazasa(self):
        return self.foglalasok
