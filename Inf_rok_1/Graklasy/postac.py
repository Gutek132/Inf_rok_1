import random
from time import sleep
class Postac():
    def __init__(self) -> None:
        self.klasa = None
        self.Lv = 0
        self.MaxHp = None
        self.Hp = None
        self.M = None
        self.MaxM = None
        self.D = []
        self.Gold = 5
        self.BHP = None
        self.BD = None
        self.Dmg = None
        self.Exp = 0
        self.Exp1 = 100
        self.Eff = 0
        self.Eff1 = None
        self.SD = 0
        self.DmgMul = 1
        self.Tura = 0
        self.Inventory = ["Wyjdź"]
        self.ParryTime = 0
        self.RageTime = 0
        self.FirePistolTime = 0
        self.FogCloudTime = 0
        self.ShieldTime = 0
        self.ShieldedDMG = 0
        self.DisarmTime = 0
        self.WeakTime = 0
        self.EnWeakTime = 0
        self.InhumanRegTime = 0
        self.WizRage = 0
        self.WizMana = 0
    def Inv(self):
        if len(self.Inventory) == 1:
            print("Nie masz nic w ekwipunku")
        else:
            print(self.Inventory)
            L = int(input("\n Wybierz którego przedmiotu chcesz użyć"))
            L1 = self.Inventory[(L - 1)]
            sleep(0.3)
            if L1 == "Wyjdź":
                print("Idziesz dalej..")
            if L1 == "Mikstura Życia":
                d = self.Hp*0.4
                if self.Hp + d > self.MaxHp:
                    d = self.MaxHp - self.Hp
                self.Hp += d
                print(f"+{d}HP")
                self.Inventory.remove("Mikstura Życia")
            if L1 == "Mikstura Szału":
                self.WizRage = 1
                print("+40% Obrażeń w następnej walce")
                self.Inventory.remove("Mikstura Szału")
            if L1 == "Mikstura Many":
                self.WizMana = 1
                print("+Nieszkończona Mana na następną walke")
                self.Inventory.remove("Mikstura Many")
    def InvGet(self, item):
        sleep(1)
        if item == "Mikstura Many":
            self.Inventory.append("Mikstura Many")
            print("Otrzymałeś [Mikstura Many]")
            self.Inventory.remove("Wyjdź")
            self.Inventory.append("Wyjdź")
        if item == "Mikstura Szału":
            self.Inventory.append("Mikstura Szału")
            print("Otrzymałeś [Mikstura Szału]")
            self.Inventory.remove("Wyjdź")
            self.Inventory.append("Wyjdź")
        if item == "Mikstura Życia":
            self.Inventory.append("Mikstura Życia")
            print("Otrzymałeś [Mikstura Życia]")
            self.Inventory.remove("Wyjdź")
            self.Inventory.append("Wyjdź")
    def Stats(self):
        print("\n ", self.klasa, "Statystyki")
        print("       Lv ", self.Lv)
        print("       HP ", self.Hp,"/",self.MaxHp)
        print("       Mana ", self.M,"/",self.MaxM)
        print("       Twoja Talia", self.D)
        print("       Złoto" , self.Gold)
        print("       Exp", self.Exp,"/",self.Exp1)