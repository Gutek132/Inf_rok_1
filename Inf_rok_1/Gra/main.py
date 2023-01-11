from time import sleep
from random import randint
STAN_KONTA = 0
money = 1
#----------------- FUNKCJE -------
def maszyna(postawiona_kwota):     #funkcja na maszyny
    global STAN_KONTA
    STAN_KONTA = STAN_KONTA - postawiona_kwota
    print(f"""
    Postawiłeś {postawiona_kwota}
    Teraz maszyna wylosuje 3 losowe symbole
    """)
    symbole = ["♠","♥","♦"]
    symbol_1 = randint(0,2)
    symbol_2 = randint(0,2)
    symbol_3 = randint(0,2)
    print(f"""
    |   |   |   |
    | {symbole[symbol_1]} | {symbole[symbol_2]} | {symbole[symbol_3]} |
    |   |   |   |
    """)
    if symbol_1 == symbol_2 == symbol_3:
        STAN_KONTA = STAN_KONTA + postawiona_kwota*20
        print("Trafiłeś 3 takie symbole! Wygrałeś!")
        print(f"Masz teraz {STAN_KONTA}$")
    else:
        print("Niestety tym razem ci się nie udało...")
        sleep(1)
#-------------------
print("="*40)
print("Witaj w potężnej grze polegającej na zdobywaniu i wydawaniu pieniędzy")
print("="*40)
while True:
    print("""
    Do którego trybu chcesz iść?
        1  | Zarabianie pieniędzy
        2  | Kasyno
        3  | Exit
    """)
    start = input("Podaj liczbę: ")
    if start == "1":
        while True:
            print("""
            Witaj w trybie, w którym zarabiasz pieniądze
            Co chcesz zrobić?
            1  | dodaje pieniądze
            2  | pokazuje stan konta
            3  | pokazuje ile $ zarabiasz na 1 klik.
            4  | sklep
            5  | zmiana trybu
            """)
            tycoon = (input("Podaj liczbę: "))
            if tycoon == "1":
                STAN_KONTA = STAN_KONTA + money
            elif tycoon == "2":
                print("...")
                print(f"Twój stan konta: {STAN_KONTA}$")
                sleep(1)
            elif tycoon == "3":
                print("...")
                print(f"Zarabiasz {money}$/klik")
                sleep(1)
            elif tycoon == "4":
                print(f"""Co chcesz kupić? Masz:{STAN_KONTA}$
                Przedmiot   | Cena | Wybór
                NIC         | NIC  | 0
                +1$/klik    | 10$  | 1
                +2$/klik    | 15$  | 2
                +5$/klik    | 30$  | 5
                +10$/klik   | 50$  | 10
                +25$/klik   | 100$ | 25
                +50$/klik   | 200$ | 50
                +100$/klik  | 300$ | 100
                +250$/klik  | 600$ | 250
                +500$/klik  | 1000$| 500
                +1000$/klik | 1800$| 1000
                """)
                wybor = (input("Wybór: "))
                if wybor == "0":
                    continue
                if wybor == "1":
                    if STAN_KONTA >= 10:
                        money = money + 1
                        STAN_KONTA = STAN_KONTA - 10
                        print("Pomyślnie zakupiono +1$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "2":
                    if STAN_KONTA >= 15:
                        money = money + 2
                        STAN_KONTA = STAN_KONTA - 15
                        print("Pomyślnie zakupiono +2$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "5":
                    if STAN_KONTA >= 30:
                        money = money + 5
                        STAN_KONTA = STAN_KONTA - 30
                        print("Pomyślnie zakupiono +5$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "10":
                    if STAN_KONTA >= 50:
                        money = money + 10
                        STAN_KONTA = STAN_KONTA - 50
                        print("Pomyślnie zakupiono +10$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "25":
                    if STAN_KONTA >= 100:
                        money = money + 25
                        STAN_KONTA = STAN_KONTA - 100
                        print("Pomyślnie zakupiono +25$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "50":
                    if STAN_KONTA >= 200:
                        money = money + 50
                        STAN_KONTA = STAN_KONTA - 200
                        print("Pomyślnie zakupiono +50$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "100":
                    if STAN_KONTA >= 300:
                        money = money + 100
                        STAN_KONTA = STAN_KONTA - 300
                        print("Pomyślnie zakupiono +100$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "250":
                    if STAN_KONTA >= 600:
                        money = money + 250
                        STAN_KONTA = STAN_KONTA - 600
                        print("Pomyślnie zakupiono +250$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "500":
                    if STAN_KONTA >= 1000:
                        money = money + 500
                        STAN_KONTA = STAN_KONTA - 1000
                        print("Pomyślnie zakupiono +500$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                elif wybor == "1000":
                    if STAN_KONTA >= 1800:
                        money = money + 1000
                        STAN_KONTA = STAN_KONTA - 1800
                        print("Pomyślnie zakupiono +1000$")
                    else:
                        print("Zakup nieudany, zbyt mało pieniędzy")
                    sleep(1)
                else:
                    print("Nie ma takiej opcji")
                    sleep(1)
                    continue
            elif tycoon == "5":
                break
            else:
                print("Nie ma takiej komendy") 
                sleep(1)
                continue
    if start == "2":
        while True:
            print("""
            Witaj w kasynie, tu możesz pomnożyć swój majątek lub go stracić
            W którą grę chciałbyś zagrać?
            1  | ruletka
            2  | suma oczek
            3  | one-armed bandit
            4  | zmiana trybu
            """)
            kasyno = input("Podaj liczbę: ")
            if kasyno == "1":
                while True:
                    print("""
                    Ruletka
                    Szybka instrukcja:
                    1. Wybierasz liczbę (od 0 do 10) i kwotę którą stawiasz
                    2. Ruletka losuje liczbę
                    3. Jeśli ruletka wylosowała twoją liczbę -> dostajesz x10 postawionej kwoty
                    Jeśli nie, tracisz postawione pieniądze.
                    """)
                    r_liczba_gracza = int(input("Podaj swoją liczbę od 0 do 10: "))
                    r_kwota_gracza = int(input(f"Podaj sumę, którą stawiasz (twój stan konta - {STAN_KONTA}$): "))
                    if r_liczba_gracza >= 1 and r_liczba_gracza <= 10 and r_kwota_gracza <= STAN_KONTA and r_kwota_gracza > 0:
                        liczba_ruletka = randint(1,10)
                        STAN_KONTA = STAN_KONTA - r_kwota_gracza
                        if liczba_ruletka == r_liczba_gracza:
                            print("="*40)
                            print("ŁO CHOLERA! TRAFIŁEŚ!")
                            r_kwota_gracza = r_kwota_gracza*10
                            STAN_KONTA = STAN_KONTA + r_kwota_gracza
                            print(f"Twój stan konta wynosi teraz {STAN_KONTA}$")
                            print("="*40)
                            sleep(1)
                            break
                        else:
                            print(f"""
                    {'='*40}
                            Ruletka wylosowała {liczba_ruletka}
                            Nie tym razem kamracie :<
                    {'='*40}
                            """)
                            sleep(1)
                            break
                    else:
                        print("="*40)
                        print("Masz podać liczbę od 0 do 10 i kwotę nie większą niż twój stan konta")
                        print("="*40)
                        sleep(1)
                        break
            elif kasyno == "2":
                while True:
                    print("""
                    Rzut kostką
                    Szybka instrukcja:
                    1. Wpisujesz ile $ chcesz postawić
                    2. Rzut kostką
                    3. Jak wypadnie parzysta liczba -> postawione pieniądze x2
                       Jeśli nie, tracisz postawione pieniądze.
                    """)
                    k_kwota_gracza = int(input(f"Podaj sumę, którą stawiasz (twój stan konta - {STAN_KONTA}$): "))
                    if k_kwota_gracza > 0 and k_kwota_gracza <= STAN_KONTA:
                        oczka = randint(1,6)
                        STAN_KONTA = STAN_KONTA - k_kwota_gracza
                        if oczka % 2 == 0:
                            print("="*51)
                            print(f"Trafiłeś liczbę {oczka}, czyli liczbę parzystą! Wygrałeś!")
                            k_kwota_gracza = k_kwota_gracza*2
                            STAN_KONTA = STAN_KONTA + k_kwota_gracza
                            print(f"Twój stan konta wynosi teraz {STAN_KONTA}$")
                            print("="*51)
                            sleep(1)
                            break
                        else:
                            print(f"""
                        {'='*44}
                            Kostka wylosowała {oczka}, więc przegrałeś
                        {'='*44}
                            """)
                            sleep(1)
                            break
                    else:
                        print("="*40)
                        print("Masz podać kwotę nie większą niż twój stan konta")
                        print("="*40)
                        sleep(1)
                        continue
            elif kasyno == "3":
                while True:
                    print("""
                    One-armed bandit
                    Szybka instrukcja:
                    1. Wybierasz maszynę (20$, 50$, 100$)
                    2. Maszyna losuje 3 symbole
                    3. Jeśli trafisz 3 takie same symbole za jednym razem -> pieniądze x20
                       Jeśli nie, tracisz pieniądze.
                    """)
                    print(f"Masz do dyspozycji {STAN_KONTA}$")
                    machine = input("Na jaką maszynę idziesz? Wybierz 20,50 lub 100: ")
                    if int(machine) > 0 and int(machine) <= STAN_KONTA:
                        if machine == "20":
                            maszyna(20)
                        elif machine == "50":
                            maszyna(50)
                        elif machine == "100":
                            maszyna(100)
                        else:
                            print("Nie ma takiej maszyny") 
                            sleep(1)
                            break
                    else:
                        print("Nie masz tyle pieniędzy") 
                        sleep(1)
                    break
            elif kasyno == "4":
                break
            else:
                print("Nie ma takiej komendy") 
                sleep(1)
                continue
    if start == "3":
        break