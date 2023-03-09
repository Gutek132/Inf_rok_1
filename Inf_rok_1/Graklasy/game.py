import random
from time import sleep
from funkcje import Funkcje
class Game():
    def __init__(self) -> None:
        self.funkcje = Funkcje()
    def game(self):
            while True:
                x = input("Wybierz Klase: \n Wojownik \n Mag \n Tank \n łucznik \n ").lower()
                if x == "wojownik":
                    self.funkcje.Wojownik()
                if x == "mag":
                    self.funkcje.Mag()
                if x == "tank":
                    self.funkcje.Tank()
                if x == "łucznik":
                    self.funkcje.Lucznik()
                while True:
                    c = random.randint(1, 3)
                    sleep(2)
                    Odp = int(input("Co chcesz zrobić \n 1. Idziesz dalej \n 2. Otwierasz ekwipunek \n 3. Sprawdź statystyki"))
                    if Odp == 2:
                        self.funkcje.Inv()
                        sleep(2)
                    if Odp == 3:
                        self.funkcje.Stats()
                        sleep(2)
                    sleep(0.5)
                    print("Idziesz dalej")
                    sleep(1.4)
                    if c == 1 or c == 3:
                        self.funkcje.BHP = 60*(1 + self.funkcje.Lv/3)
                        print(f"\n Napotkałeś agresywnego bandyte! ({self.funkcje.BHP} HP)")
                        #Na dole pętla walki
                        sleep(0.2)
                        self.funkcje.CombatSystem("Bandyta", 60, 10, 1, 1, 2, 1, 2)
                        ran = random.randint(1, 100)
                        if ran >= 65:
                            ran2 = random.randint(1, 3)
                            if ran2 == 1:
                                self.funkcje.InvGet("Mikstura Szału")
                            if ran2 == 2:
                                self.funkcje.InvGet("Mikstura Many")
                            if ran2 == 3:
                                self.funkcje.InvGet("Mikstura Życia")
                        
                    if c == 2:
                        print("W oddali widzisz karczme, postanawiasz się tam udać ")
                        sleep(1.4)
                        dc = int(input("Wchodzisz do karczmy, co robisz \n 1. [Zostań na noc i zregeneruj 25% HP za 8 Złota] \n 2. [Posiedz w karczmie] \n 3. [Wyjdź] \n "))
                        while True:
                            if dc == 1:
                                if self.funkcje.Gold >= 8:
                                    self.funkcje.Gold -= 8
                                    HPRG = self.funkcje.MaxHp*0.25
                                    self.funkcje.Hp += HPRG
                                    if self.funkcje.Hp > self.funkcje.MaxHp:
                                        self.funkcje.Hp = self.funkcje.MaxHp
                                    if HPRG + self.funkcje.Hp > self.funkcje.MaxHp:
                                        HPRG = self.funkcje.MaxHp - self.funkcje.Hp
                                    print(f"\n Zostałeś na noc\n +{HPRG} HP \n -8 Złota ")
                                    break
                                else:
                                    print("Nie masz wystarczająco pieniędzy, wybierz ponownie")
                                    dc = input
                            if dc == 2:
                                print("")
                                print("1. Zostałeś okradziony i straciłeś 5 złota \n 2. Wdałeś się w bójkę z lokalnym pijakiem\n 3. Zostałeś wyrzucony \n 4. Grasz w karty \n 5. Wygrałeś zakład i otrzymałeś 6 sztuk Złota \n 6. Spotykasz hojnego maga ")
                                sleep(1)
                                input("[Rzuć kością]")
                                print("Losowanie...")
                                sleep(1.2)
                                g = random.randint(1, 6)
                                print(f"Wylosowałeś {g}")
                                if g == 1:
                                    go = round(5, 0)
                                    self.funkcje.Gold -= go
                                    print(f"Zostałeś okradziony! \n -{go} Złoto")
                                    break
                                if g == 2:
                                    print("Wdałeś się w bójkę z lokalnym pijakiem  ")
                                    self.funkcje.BHP = 60*(1+(self.funkcje.Lv/3))
                                    self.funkcje.BHP = round(self.funkcje.BHP, 0)
                                    self.funkcje.CombatSystem("Pijak", 50, 8, 2, 1, 2, 1, 2)
                                if g == 3:
                                    print("\n Zostałeś wyrzucony!")
                                    break
                                if g == 4:
                                    print("")
                                    print("grasz w karty z lokalnym bogaczem, obaj rzucacie trzy razy kością, osoba z większą ilością punktów wygrywa")
                                    sleep(1)
                                    while True:
                                        if self.funkcje.Gold <= 0:
                                            print("Nie masz pieniędzy")
                                            break
                                        Reward = input("Ile złota chcesz obstawić")
                                        if int(Reward) <= 0:
                                            print("Obtawiłeś wogle jakieś Złoto??? Bogacz uznaje to za obraze i zostajesz wyrzucony z karczmy")
                                        if int(Reward) <= self.funkcje.Gold:
                                            npc = 0
                                            player = 0
                                            sleep(1)
                                            for i in range(3):
                                                print("Przeciwnik losuje liczbe")
                                                d = random.randint(1, 6)
                                                npc += d
                                                sleep(1)
                                                print(f"Wylosował {d}")
                                                input("[Rzuć kością]")
                                                print("Losowanie...")
                                                d = random.randint(1, 6)
                                                player += d
                                                sleep(1)
                                                print(f"Wylosowałeś {d}")
                                                sleep(1)
                                            if npc > player:
                                                print(f"Przegrałeś zakład \n -{Reward} Gold")
                                                self.funkcje.Gold -= int(Reward)
                                                break
                                            if npc == player:
                                                print("Remis! Nic nie tracisz ani nic nie wygrywasz")
                                                break
                                            if player > npc:
                                                print(f"Wygrałeś zakład! \n +{Reward} Gold")
                                                self.funkcje.Gold += int(Reward)
                                                break
                                        else:
                                            print("Nie masz pieniędzy")
                                if g == 5:
                                    print("Wygrałeś zakład \n +6 Gold")
                                    self.funkcje.Gold += 6
                                    break
                                if g == 6:
                                    print("Spotykasz hojnego maga")
                                    sleep(1)
                                    print("Pozwala ci wybrać jedną z jego mikstur")
                                    gift = int(input("1. Mikstura Szału [+40% brażeń przez następną walke] \n 2. Mikstura Leczenia [Ulecz 40% HP] \n 3. Mikstura Many [Nieskończona mana na następną walke] "))
                                    if gift == 1:
                                        print("Podziękowałeś Magowi i przyjąłeś miksture szału")
                                        self.funkcje.InvGet("Mikstura Szału")
                                    if gift == 2:
                                        print("Podziękowałeś Magowi i przyjąłeś miksture Życia")
                                        self.funkcje.InvGet("Mikstura Życia")
                                    if gift == 3:
                                        print("Podziękowałeś Magowi i wprzyjąłeś miksture many")
                                        self.funkcje.InvGet("Mikstura Many")

                            print("Wychodzisz z karczmy")
                            sleep(1.3)
                            break

                    if 0 >= self.funkcje.Hp:
                        sleep(1.5)
                        print("Ładowanie nowej gry...\n")
                        sleep(2)
                        break
                        
                    