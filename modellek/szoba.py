from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_ar(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(5000, szobaszam)

    def get_ar(self):
        return self.ar


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(8000, szobaszam)

    def get_ar(self):
        return self.ar
