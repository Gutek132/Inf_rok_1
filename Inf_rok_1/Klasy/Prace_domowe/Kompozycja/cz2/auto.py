from silnik import Silnik
from akumulator import Akumulator
from opony import Opony
from skrzynia_biegow import Skrzynia_biegow

class Auto:
    def __init__(self, wlasciciel : str) -> None:
        self.__wlascicel = wlasciciel
        self.__akumlator = Akumulator()
        self.__silnik = Silnik()
        self.__opony = Opony()
        self.__skrzynia_biegow = Skrzynia_biegow()

    def all_information(self):
        print("="*40)
        print(self.__wlascicel)
        self.__akumlator.informacje()
        self.__silnik.informacje()
        self.__opony.informacje()
        self.__skrzynia_biegow.informacje()
        print("="*40)

    def zmien_informacje(self):
        print("co chcesz zmienic")
        print("a - silnik")
        print("b - akumulator")
        print("c - opony")
        print("d - skrzynia biegow")
        inp = input().lower().strip()
        if inp == "a":
            self.__silnik.zmien_informacje_silnik()
        elif inp == "b":
            self.__akumlator.zmien_dane_akumolatora()
        elif inp == "c":
            self.__opony.zmien_dane_opon()
        elif inp == "d":
            self.__skrzynia_biegow.zmien_dane_skrzyni_biegow()

    def brrrbrrrr(self):
        self.__silnik.brrrbrrrr()
        