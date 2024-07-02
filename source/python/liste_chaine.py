class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        return "("+str(self.valeur)+"," +str(self.suivant)+")"

class Liste:
    def __init__(self):
        self.maillon = None

    def est_vide(self):
        return self.maillon == None
    
    def inserer(self,element):
        nouveau_maillon = Maillon(element,self.maillon)
        self.maillon = nouveau_maillon

    def tete(self):
        if not self.est_vide():
            return self.maillon.valeur

    def queue(self):
        fin_de_liste = None
        if not self.est_vide():
            fin_de_liste = Liste()
            fin_de_liste.maillon = self.maillon.suivant
        return fin_de_liste
        
    def __repr__(self):
        if self.est_vide():
            return "[]"
        else:
            return "["+str(self.tete())+"]->"+str(self.queue())

def creer_liste_chaine():
    return Liste()

if __name__ == "__main__":
    L = creer_liste_chaine()
    L.inserer(4)
    L.inserer(7)
    L.inserer(1)
    print(L.est_vide())
    print(L)
    a,b = L.tete(),L.queue()
    print(a)
    print(b)


maillon = Maillon(9)
L

maillon.suivant

maillon.suivant = L.maillon.suivant.suivant

L.maillon.suivant = maillon

L

a = Maillon(1)
b = Maillon(7)
c = Maillon(4)

a.suivant = b
b.suivant = c

a.suivant

a

d = Maillon(5)
c.suivant=d
a

e = Maillon(3)
e.suivant=a

e

e.suivant.suivant.suivant

L=creer_liste_chaine()

L.maillon = e

L.inserer(2)

L




