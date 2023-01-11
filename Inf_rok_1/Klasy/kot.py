class Kot():
    masa_ciala = 0
    wiek = 0
    imie = ""
    plec = True
    kolor_siersci = ""
    kolor_oczu = ""
    dlugosc_ogona = 0
    puszystosc = "" 
    rodzaj_siersci = ""

    def nazwij_kota(self):
        self.imie = input("")
    def wpisz_wage(self):
        self.masa_ciala = input("")
    def wpisz_wiek(self):
        self.wiek = input("")
    def inf_imie(self):
        print(self.imie)
    def okresl_plec(self):
        inp_plec = input("1 - Male| 2 - Female: ")
        if inp_plec == "1":
            self.plec = "Male"
        elif inp_plec == "2":
            self.plec = "Female"
    def wybierz_kolor_siersci(self):
        self.kolor_siersci = input("")
    def wybierz_kolor_oczu(self):
        self.kolor_oczu = input("")
    def wpisz_dlugosc_ogona(self):
        self.dlugosc_ogona = input("")
    def wybierz_puszystosc(self):
        self.puszystosc = input("")
    def wybierz_rodzaj_siersci(self):
        self.rodzaj_siersci = input("")