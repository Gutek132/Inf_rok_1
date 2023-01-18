class Skrzynia_biegow:
    def __init__(self) -> None:
        self.__ilosc_biegow = None
        self.__automat = None
        self.__firma = None

    def informacje(self):
        print("Dane skrzyni biegów")
        print(self.__ilosc_biegow)
        print(self.__firma)
        print(self.__automat)    

    def zmien_dane_skrzyni_biegow(self):
        while True:
            print("="*40)
            print("a - ilosc biegow")
            print("b - firma")
            print("c - automat")
            inp = input().lower().strip()
            if inp == "a":
                inp = input().lower().strip()
                self.__ilosc_biegow = inp
            if inp == "b":
                inp = input().lower().strip()
                self.__firma = inp
            if inp == "c":
                inp = input().lower().strip()
                self.__automat = inp
            else:
                continue