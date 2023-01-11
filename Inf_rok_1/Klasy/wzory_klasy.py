from math import pi


class Wzory():
 
    def __init__(self,a,b,c,Pp,Pb,r,H,l) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.Pp = Pp
        self.Pb = Pb
        self.r = r
        self.H = H
        self.l = l
        self.poleSzes = self.oblicz_poleSzes(self.a)
        self.poleProstopadłościanu = self.oblicz_poleProstopadłościanu(self.a,self.b,self.c)
        self.poleGraniastosłupa = self.oblicz_poleGraniastosłupa(self.Pp,self.Pb)
        self.poleOstrosłupa = self.oblicz_poleOstrosłupa(self.Pp,self.Pb)
        self.poleWalca = self.oblicz_poleWalca(self.r)
        self.poleStożka = self.oblicz_poleStożka(self.r,self.l)
        self.poleKuli = self.oblicz_poleKuli(self.r)
        self.VSzes = self.oblicz_VSzes(self.a)
        self.VProstopadłościanu = self.oblicz_VProstopadłościanu(self.a,self.b,self.c)
        self.VGraniastosłupa = self.oblicz_VGraniastosłupa(self.Pp,self.H)
        self.VOstrosłupa = self.oblicz_VOstrosłupa(self.Pp,self.H)
    def oblicz_poleSzes(a):
        print(6*(a**2))
    #----------
    def oblicz_poleProstopadłościanu(a,b,c):
        print(2*a*b+2*a*c+2*b*c)
    #----------
    def oblicz_poleGraniastosłupa(Pp,Pb):
        print(2*Pp+Pb)
    #----------
    def oblicz_poleOstrosłupa(Pp,Pb):
        print(Pp+Pb)
    #----------
    def oblicz_poleWalca(r):
        print(2*pi*r**2)
    #----------
    def oblicz_poleStożka(r,l):
        print(pi*r**2+pi*r*l)
    #----------
    def oblicz_poleKuli(r):
        print(4*pi*r**2)
    #----------
    def oblicz_VSzes(a):
        print(a**3)
    #----------
    def oblicz_VProstopadłościanu(a,b,c):
        print(a*b*c)
    #----------
    def oblicz_VGraniastosłupa(Pp,H):
        print(Pp*H)
    #----------
    def oblicz_VOstrosłupa(Pp,H):
        print(1/3*Pp*H)




