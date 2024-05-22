class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def hozzaad_szoba(self, szoba):
        self.szobak.append(szoba)

    def get_szobak(self):
        return self.szobak
