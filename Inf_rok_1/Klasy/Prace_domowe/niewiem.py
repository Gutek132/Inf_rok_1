class zadanie1():
    @staticmethod
    def wyswietlwszystko():
        with open('plik.txt','r') as myfile:
            obj = myfile.read()
            print(obj)
    @staticmethod
    def dawajkolejnolinikami():
        with open('plik.txt','r') as myfile:
            for i in myfile:
                print(i)
    @staticmethod
    def kolejnoliterami():
        with open('plik.txt','r') as myfile:
            objekt = myfile.read()
            for i in objekt:
                print(i)
    @staticmethod
    def codrugiznak():
        with open('plik.txt','r') as myfile:
            for i in myfile:
                print(i[::2])
    @staticmethod
    def tosamocoinput():
        inp = input('dej litere ').lower()
        print()
        with open('plik.txt', 'r') as myfile:
            calytekst = myfile.read()
            for litera in calytekst:
                if inp == litera.lower():
                    print(litera)
    @staticmethod
    def identycznalinijka():
        inp = input('dej litere ').lower()
        print()
        with open('plik.txt', 'r') as myfile:
            for linijka in myfile:
                if inp in linijka:
                    print(linijka)
    @staticmethod
    def pierwszeznaki():
        with open('plik.txt','r') as myfile:
            Ouagadougou = myfile.read()
            print(Ouagadougou[0:10])
    @staticmethod
    def ostatnieznaki():
        with open('plik.txt','r') as myfile:
            Ouagadougou = myfile.read()
            print(Ouagadougou[-1:-10:-1])
    @staticmethod
    def jileznakow():
        with open('plik.txt','r') as myfile:
            ilosca = 0
            iloscb = 0
            iloscc = 0
            for linia in myfile:
                for litera in linia:
                    if litera == 'a':
                        ilosca += 1
                    if litera == 'b':
                        iloscb += 1
                    if litera == 'c':
                        iloscc += 1
            print('ilosc a = ',ilosca)
            print('ilosc b = ',iloscb)
            print('ilosc c = ',iloscc)
class zadanie2():
    @staticmethod
    def pisz():
        with open('plik.txt','r') as plik1:
            tekst = plik1.read()
        with open('plik2.txt','w') as plik2:
            plik2.write(tekst)
    @staticmethod
    def napisz():
        with open('plik2.txt','r') as plik2:
            tekst = plik2.read()
        with open('plik3.txt','w') as plik3:
            plik3.write(tekst[::2])
    @staticmethod
    def dopisz():
        with open('plik2.txt','r') as plik2:
            tekst = plik2.read()
        with open('plik4.txt','w') as plik4:
            inp = int(input('ile razy '))
            for i in range(inp):
                plik4.write(tekst)
class zadanie3():
    @staticmethod
    def drob():
        ile = int(input('ile tego chcesz (nie rob duzo bo bluescreena wywali) '))
        for ile in range(ile):
            with open(f'plikdozadanie4i{ile+1}.tct','w') as myfile:
                myfile.write(f'kocham_inf {ile+1}')
class zadanie4():
    @staticmethod
    def odwracajsiedogurynogami():
        with open('plik.txt','r') as plik1:
            czyt = plik1.read()
        with open('plikzodwroconakolejnoscia.txt','w') as plik2:
            plik2.write(czyt[::-1])
class zadanie5():
    @staticmethod
    def duzoinputow():
        inpn= int(input('ile plikow '))
        inpk= str(input('jaka nazwa '))
        inpm= int(input('ile linijek '))
        inpzawartosc= str(input('jaka zawartosc '))
        
        for inpn in range(inpn):
            with open(f'{inpk}{inpn+1}.txt','w') as myfile:
                linijki = inpm
                for linijki in range(inpm):
                    myfile.write(f'{inpzawartosc} \n')
class zadanie6():
    @staticmethod
    def listapista():
        lista = [i for i in range(1,10+1)]
        inp= int(input('ile linijek '))
        with open('generatorlist.txt','w') as myfile:
            for i in range(inp):
                myfile.write(f'{lista} \n')
class zadanie7():
    @staticmethod
    def tabliczkaczekolady():
        inp = int(input('jaka wielkosc '))
        with open('tabliczkaniemnozenia.txt','w') as myfile:
            for i in range(1,inp+1):
                for n in range(1,inp+1):
                    myfile.write(f'{i*n}\t')
                myfile.write('\n')
class zadanie8():
    @staticmethod
    def wszystkonaraz():
        with open('Classified_Documents.txt','w') as myfile:
            imie = str()
            nazwisko = str()
            miasto = str()
            telefon = str()
            while True:
                print('\nCo zmieniasz?')
                print('i - imie')
                print('n - nazwisko')
                print('m - miasto')
                print('t - telefon')
                print('e - eggsit')
                inp = input()
                if inp == 'i':
                    imie = input('dej imie ')
                if inp == 'n':
                    nazwisko = input('dej nazwisko ')
                if inp == 'm':
                    miasto = input('dej miasto ')
                if inp == 't':
                    telefon = input('dej telefon ')
                if inp == 'e':
                    myfile.write(f'Imie: {imie}, Nazwisko: {nazwisko}, Miasto: {miasto}, Telefon: {telefon[0:9]}')
                    break
                else:
                    print('\nERROR 404 Not Found')