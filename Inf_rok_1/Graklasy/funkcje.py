import random
from time import sleep
from postac import Postac

class Funkcje(Postac):
    def Wojownik(self):
            self.klasa = "Wojownik"
            self.MaxHp = 120
            self.Hp = 120
            self.M = 25
            self.MaxM = 25
            self.D.append("Uderzenie (+5M)")
            self.D.append("Riposta (-5M)")
            self.D.append("Combo (-10M)")
            self.D.append("Szał (-10M)")
    def Mag(self):
            self.klasa = "Mag"
            self.MaxHp = 80
            self.Hp = 80
            self.M = 60
            self.MaxM = 60
            self.D.append("Ognista Kula (-5M)")
            self.D.append("Odnowienie many (+30M)")
            self.D.append("Zasłona Dymna (-15M)")
            self.D.append("Słabe uleczenie (-10M)")
    def Tank(self):
            self.klasa = "Tank"
            self.MaxHp = 140
            self.Hp = 140
            self.M = 20
            self.MaxM = 20
            self.D.append("Uderzenie (+5M)")
            self.D.append("Tarcza (+? M)")
            self.D.append("Uderzenie tarczą (-15M)")
            self.D.append("Szybkie uleczenie (-10M)")
    def Lucznik(self):
            self.klasa = "Łucznik"
            self.MaxHp = 90
            self.Hp = 90
            self.M = 40
            self.MaxM = 40
            self.D.append("Strzał (+5M)")
            self.D.append("Rozbrojenie (-10M)")
            self.D.append("Zasłona Dymna (-15M)")
            self.D.append("Strzał Losu (0M)")
    def Lev(self,t):
        self.Exp += t
        while True:
            if self.Exp1 <= self.Exp:
                self.Lv += 1
                self.Exp -= self.Exp1
                print(f"Osiągnołeś {self.Lv} Lv \n")
                self.Exp1 += 30
                self.MaxHp += 10
                self.Hp += 10
                self.MaxM += 5
                self.M += 5
            else:
                break
            
    def Moves(self,m):
        if m == "Uderzenie (+5M)": 
            self.M += 5
            if self.M > self.MaxM:
                self.M = self.MaxM
            self.Dmg = (11 + self.Lv*2)*self.DmgMul
            self.Dmg = round(self.Dmg, 1)
            self.BHP -= self.Dmg
            print(f"\n Zadałeś {self.Dmg} Obrażeń! (przeciwnik ma {self.BHP} HP)  \n")
            
        if m == "Riposta (-5M)":
            if self.M >= 5:
                self.M -= 5
                self.Eff = 1
                self.Eff1 = 1
                self.ParryTime = 1
                print("\n Użyłeś Riposty, następny atak przeciwnika zadaje 50% mniej obrażeń, odbijasz 50% pierwotnych obrażeń\n")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Combo (-10M)":
            if self.M >= 10:
                self.M -= 10
                for i in range(3):
                    a = 2+(1+(self.Lv/2))
                    b = 9+(1+(self.Lv/2))
                    c = random.randint(4, 8)
                    c = c*(1+(self.Lv/3))
                    c = round(c, 1)
                    c = c*self.DmgMul
                    print(f"\n Zadałeś {c} obrażeń!")
                    self.BHP -= c
                print(f"przeciwnik ma {self.BHP} HP")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Szał (-10M)":
            if self.M >= 10 and self.RageTime == 0:
                self.M -= 10
                self.RageTime += 3
                self.DmgMul += 0.7
                print("\n Użyłeś Szału, twoje obrażenia są o 70% większe przez 2 tury")
            else:
                print("Nie masz wystarczająco many by tego użyć lub masz już uaktywniony Szał")
                self.AS()    
        if m == "Ognista Kula (-5M)":
            if self.M >= 5:
                self.M -= 5
                self.Dmg = (10 + self.Lv*2)*self.DmgMul
                self.Dmg = round(self.Dmg, 1)
                self.BHP -= self.Dmg
                self.FirePistolTime = 2
                print(f"\n Zadałeś {self.Dmg} obrażeń i podpaliłeś przeciwnika na dwie tury  (przeciwnik ma {self.BHP} HP)  \n")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Odnowienie many (+30M)":
            self.M += 30
            dg = 30
            if self.M > self.MaxM:
                dg = 30 - (self.MaxM - self.M)
                self.M = self.MaxM
            print(f"Odnowiłeś {dg} Many")
        if m == "Słabe uleczenie (-10M)":
            if self.M >= 10:
                self.M -= 10
                p = round(self.MaxHp * 0.15, 0) + 2
                self.Hp += p
                if self.Hp >= self.MaxHp:
                    self.Hp = self.MaxHp
                print(f"Wyleczyłeś {p} HP, teraz masz {self.Hp} HP!")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Zasłona Dymna (-15M)":
            if self.M >= 15:
                self.M -= 15
                self.FogCloudTime = 2
                print(f"Użyłeś Zasłony dymnej, teraz nasz 70% na uniknięcie 2 następnych ataków ")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Tarcza (+? M)":
                self.ShieldTime = 1
                print("Użyłeś Tarczy, następny wrogi atak zadaje 80% mniej obrażeń, otrzymujesz też mane w wysokości połowy osłoniętych obrażeń")
        if m == "Szybkie uleczenie(-10M)":
            if self.M >= 10:
                self.M -= 10
                p = 3 + round(self.MaxHp*0.12, 0)
                self.Hp += p
                if self.Hp >= self.MaxHp:
                    self.Hp = self.MaxHp
                print(f"Wyleczyłeś {p} HP, teraz masz {self.Hp} HP!")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Uderzenie tarczą (-15M)":
            if self.M >= 10:
                self.M -= 10
                d = (self.ShieldedDMG * 0.9)*self.DmgMul
                self.BHP -= round(d, 1) + 5
                self.ShieldedDMG = 0
                print(f"Zadajesz obrażenia równe 90% obrażeń zablokowanych przez tarcze plus 5, zadałeś {round(d, 1)  + 5} obrażeń, Zablokowane obrażenie zresetowane")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Strzał (+5M)":
            self.M += 5
            if self.M > self.MaxM:
                self.M = self.MaxM
            self.Dmg = (13 + self.Lv*2)*self.DmgMul
            self.Dmg = round(self.Dmg, 1)
            self.BHP -= self.Dmg
            print(f"\n Zadałeś {self.Dmg} Obrażeń! (przeciwnik ma {self.BHP} HP)  \n")
            
        if m == "Rozbrojenie (-10M)":
            if self.M >= 10:
                self.M -= 10
                d = (5*(1 + self.Lv/2))*self.DmgMul
                self.DisarmTime = 1
                self.WeakTime = 3
                self.BHP -= round(d, 1)
                print(f"Rozbroiłeś wroga, zadałeś {round(d, 1)}, Ogłuszyłeś go i nadałeś mu efekt [Słabość] na 2 tury")
            else:
                print("Nie masz wystarczająco many by tego użyć")
                self.AS()
        if m == "Strzał Losu (0M)":
                Los = random.randint(1, 10)
                if Los <= 5:
                    self.Dmg = (10+ self.Lv*2)*self.DmgMul
                    self.BHP -= self.Dmg
                    print(f"\n Użyłeś zwykłej strzały, zadałeś {self.Dmg} obrażeń!  (przeciwnik ma {self.BHP} HP)  \n")
                if Los > 5 and Los < 8:
                    self.M += 10
                    if self.M > self.MaxM:
                        self.M = self.MaxM
                    self.DisarmTime = 1
                    print(f"\n Użyłeś strzały pełnej energii, ogłuszasz przeciwnika na 1 turę i regenerujesz 10 Many")
                if Los > 7 and Los < 10:
                    self.FirePistolTime = 3
                    self.Dmg = (10 + self.Lv*2)*self.DmgMul
                    self.BHP -= round(self.Dmg, 1)
                    print(f"Użyłeś ognistej strzały i podpaliłeś przeciwnika na dwie tury, (przeciwnik ma {self.BHP} HP) ")
                if Los == 10:
                    self.Dmg = (35 + self.Lv*4)*self.DmgMul
                    self.M += 5
                    self.BHP -= round(self.Dmg, 1)
                    if self.M > self.MaxM:
                        self.M = self.MaxM
                    print(f"Strzeliłeś prosto w głowe! Zadałeś {self.Dmg} and i odnowiłeś 5 Many, Przeciwnik ma {self.BHP} HP")

    def CombatSystem(self, Name, Exp, Gol, Type, Att1, Att2, Att3, Att4):
        while True:
                self.Timere(0)
                self.Tura += 1
                sleep(2.5)
                print(f"---------------------------- Tura {self.Tura} ---------------------------- \n ")
                a = random.randint(1, 4)
                print(f" {self.D}")
                self.AS()
                print("")
                sleep(1)
                if self.BHP <= 0:
                    sleep(1)
                    print(f"{Name} został pokonany")
                    self.Timere(1)
                    vc = random.randint((Gol - 5), Gol)
                    self.Gold += vc
                    print(f"Otrzymałeś {vc} złota")
                    self.Lev(Exp)
                    print(f"Otrzymałeś {self.Exp} Exp\n")
                    self.Tura = 0
                    break
                if a == 1:
                    self.EnMoves(Type, Att1)
                    #Zwykle uderzenie
                elif a == 2:
                    self.EnMoves(Type, Att2)
                    #zabranie golda
                elif a == 3:
                    self.EnMoves(Type, Att3)
                elif a == 4:
                    self.EnMoves(Type, Att4)
                if self.Hp <= 0:
                        sleep(1)
                        print("\n YOU DIED \n")
                        return 
                if self.SD != 0:
                    self.BHP -= self.SD
                    sleep(1)
                    print(f"{Name} dostał {self.SD} obrażeń")
                    self.SpecEff(self.Eff1)
                    if self.BHP <= 0:
                        sleep(1)
                        print(f"{Name} został pokonany")
                        self.Timere(1)
                        vc = random.randint((Gol - 5), Gol)
                        self.Gold += vc
                        print(f"Otrzymałeś {vc} złota\n")
                        self.Lev(self.Exp)
                        self.Tura = 0
                        break
    def SpecEff(self, n):
        #Parry
        if self.ParryTime == 1:
            self.SD += self.BD*0.5
            self.SD = round(self.SD, 1)
            self.BD = self.BD*0.5
            self.BD = round(self.BD, 1)
        if self.FogCloudTime >= 1:
            p = random.randint(1, 100)
            if p >= 31:
                self.BD = 0
        if self.ShieldTime >= 1:
            c = self.BD * 0.8
            self.ShieldedDMG += c 
            self.BD = self.BD *0.2
            self.BD = round(self.BD, 1)
            self.M += round(c*0.5, 1)
            if self.M >= self.MaxM:
                self.M = self.MaxM
        if self.DisarmTime >= 1:
            self.BD = 0
        if self.WeakTime >= 1:
            self.BD = round(self.BD*0.8, 1)
            
        
    def EnMoves(self, M, a):
        if M == 1:
            if a == 1:
                self.BD = random.randint(5 + (self.Lv*2), 10 + (self.Lv*2))
                if self.ParryTime <= 1 or self.FogCloudTime >= 1 or self.ShieldTime >= 1:
                    self.SpecEff(0)
                self.Hp -= self.BD
                sleep(1)
                print(f"\n Bandyta użył pchnięcia, zadał {self.BD} Obrażeń, teraz masz {self.Hp} HP")
            if a == 2:
                self.BD = 7*(1 + self.Lv/2)
                if self.ParryTime <= 1 or self.FogCloudTime >= 1 or self.ShieldTime >= 1:
                    self.SpecEff(0)
                self.Hp -= self.BD
                stel = random.randint(0,1)
                self.Gold -= stel
                sleep(1)
                print(f"\n Bandyta użył Złodziejstwa , zadał {self.BD} obrażeń i ukradł {stel} złota, teraz masz {self.Hp} HP \n")
        if M == 2:
            if a == 1:
                self.BD = random.randint(6 + (self.Lv*2), 11 + (self.Lv*2))
                if self.ParryTime <= 1 or self.FogCloudTime >= 1 or self.ShieldTime >= 1:
                    self.SpecEff(0)
                self.Hp -= self.BD
                sleep(1)
                print(f"\n Pijak użył pchnięcia i zadał {self.BD} obrażeń, teraz masz {self.Hp} HP")
            if a == 2:
                self.BD = 6*(1 + self.Lv/2)
                if self.EnWeakTime == 0:
                    self.DmgMul -= 0.2
                self.EnWeakTime = 3
                if self.ParryTime <= 1 or self.FogCloudTime >= 1 or self.ShieldTime >= 1:
                    self.SpecEff(0)
                self.Hp -= self.BD
                sleep(1)
                print(f"\n pijak użył rozbicia butelki i zadał {self.BD} obrażeń i nałożył na ciebie efekt [Słabość], teraz masz {self.Hp} HP \n")
                
    def Timere(self, Ded):
        #Parry
        if self.ParryTime <= 1 or Ded == 1:
            self.ParryTime = 0
            self.SD = 0
            self.Eff1 = 0
            self.BD = self.BD
        if self.RageTime >= 1:
            self.RageTime = self.RageTime - 1
            if self.RageTime == 0 or Ded == 1:
                self.DmgMul -= 0.7
        if self.FirePistolTime >= 1:
            self.FirePistolTime -= 1
            minid = 5 + self.Lv*2
            self.BHP -= minid
            print(f"Przeciwnik został dotknięty ogniem za {minid} obrażeń, teraz ma {self.BHP} HP")
            if self.FirePistolTime <= 0 or Ded == 1:
                self.FirePistolTime = 0
        if self.FogCloudTime >= 1 or Ded == 1:
            if self.BD == 0:
                print("Uniknąłeś ataku przeciwnika!")
            self.FogCloudTime -= 1
        if self.ShieldTime >= 1:
            self.ShieldTime -= 1
            print(f"Osłoniłeś się przed atakiem przeciwnika, teraz masz {self.M} Many i {self.Hp} HP")
        if self.DisarmTime >= 1:
            self.DisarmTime = 0
            print("Przeciwnik jest ogłuszony")
        if self.WeakTime >= 1:
            self.WeakTime -= 1
            if Ded == 1:
                self.WeakTime = 0
        if self.EnWeakTime >= 1:
            self.EnWeakTime -= 1
            if Ded == 1 or self.EnWeakTime == 0:
                self.DmgMul += 0.2
        if self.InhumanRegTime >= 1:
            p = self.BD*0.5
            self.InhumanRegTime -= 1
            self.Hp += p
            if self.Hp > self.MaxHp:
                self.Hp = self.MaxHp
            print(f"+{p}HP, teraz masz {self.Hp} HP")
        if self.WizRage == 1:
            self.DmgMul += 0.4
            self.WizRage = 2
        if self.WizMana ==  1:
            self.M = self.MaxM
            if Ded == 1:
                self.WizMana = 0
        if Ded == 1 and self.WizRage >= 2:
            self.DmgMul -= 0.4
            self.WizRage = 0
        self.Hp = round(self.Hp, 1)
        self.BHP = round(self.BHP, 1)

    def AS(self):
        L = int(input("\n Wybierz umiejętność od 1 do 4 "))
        L1 = self.D[(L - 1)]
        sleep(0.3)
        self.Moves(L1)

    