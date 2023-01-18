class Opony:
    def __init__(self) -> None:
        self.__typ = None
        self.__wielkosc = None
        self.__felgi = None

    def informacje(self):
        print("Dane opon")
        print(self.__typ)
        print(self.__wielkosc)
        print(self.__felgi)    

    def zmien_dane_opon(self):
        while True:
            print("="*40)
            print("a - typ")
            print("b - wielkosc")
            print("c - felgi")
            inp = input().lower().strip()
            if inp == "a":
                inp = input().lower().strip()
                self.__typ = inp
            if inp == "b":
                inp = input().lower().strip()
                self.__wielkosc = inp
            if inp == "c":
                inp = input().lower().strip()
                self.__felgi = inp
            else:
                continue