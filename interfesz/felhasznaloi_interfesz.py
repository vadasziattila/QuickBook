from datetime import datetime
from modellek.szoba import EgyagyasSzoba, KetagyasSzoba
from modellek.szalloda import Szalloda
from modellek.foglalas import FoglalasKezelo


def felhasznaloi_interfesz():
    szalloda = Szalloda("Példa Szálloda")
    foglalas_kezelo = FoglalasKezelo()

    # Szobák hozzáadása
    szalloda.hozzaad_szoba(EgyagyasSzoba(101))
    szalloda.hozzaad_szoba(KetagyasSzoba(102))
    szalloda.hozzaad_szoba(EgyagyasSzoba(103))

    # Példa foglalások hozzáadása
    foglalas_kezelo.foglalas_letrehozasa(szalloda.szobak[0], datetime(2024, 6, 1))
    foglalas_kezelo.foglalas_letrehozasa(szalloda.szobak[1], datetime(2024, 6, 2))
    foglalas_kezelo.foglalas_letrehozasa(szalloda.szobak[2], datetime(2024, 6, 3))
    foglalas_kezelo.foglalas_letrehozasa(szalloda.szobak[0], datetime(2024, 6, 4))
    foglalas_kezelo.foglalas_letrehozasa(szalloda.szobak[1], datetime(2024, 6, 5))

    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Adja meg a választott művelet számát: ")

        if valasztas == "1":
            try:
                szobaszam = int(input("Adja meg a szobaszámot: "))
                datum = input("Adja meg a dátumot (YYYY-MM-DD): ")
                datum = datetime.strptime(datum, "%Y-%m-%d")
                szoba = next(sz for sz in szalloda.get_szobak() if sz.szobaszam == szobaszam)
                ar = foglalas_kezelo.foglalas_letrehozasa(szoba, datum)
                print(f"Sikeres foglalás! A szoba ára: {ar} Ft")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif valasztas == "2":
            try:
                szobaszam = int(input("Adja meg a szobaszámot: "))
                datum = input("Adja meg a dátumot (YYYY-MM-DD): ")
                datum = datetime.strptime(datum, "%Y-%m-%d")
                szoba = next(sz for sz in szalloda.get_szobak() if sz.szobaszam == szobaszam)
                foglalas_kezelo.foglalas_lemondasa(szoba, datum)
                print("Sikeres lemondás!")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif valasztas == "3":
            foglalasok = foglalas_kezelo.foglalasok_listazasa()
            if foglalasok:
                for foglalas in foglalasok:
                    print(f"Szoba szám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")
            else:
                print("Nincs foglalás.")

        elif valasztas == "4":
            break

        else:
            print("Érvénytelen választás.")
