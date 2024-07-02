class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return "["+str(self.valeur)+"]->" + "[]"
        else:
            return "["+str(self.valeur)+"]->" +str(self.suivant)
        
class Liste:
    
    def __init__(self):
        self.maillon = None
        
    def est_vide(self):
        return self.maillon == None
    
    def tete(self):
        if not self.est_vide():
            return self.maillon.valeur
        
    def queue(self):
        q = Liste()
        if not self.est_vide():
            q.maillon = self.maillon.suivant
        return q
    
    def inserer(self,element):
        nv_maillon = Maillon(element)
        nv_maillon.suivant = self.maillon
        self.maillon = nv_maillon
        
    def __repr__(self):
        if self.maillon == None:
            return "[]"
        else:
            return str(self.maillon)
        
def longueur(liste_chaine:Liste) -> int:
    if liste_chaine.est_vide():
        return 0
    else:
        long = 0
        while not(liste_chaine.est_vide()):
            liste_chaine = liste_chaine.queue()
            long += 1
        return long

def atteint(liste_chaine:Liste,n:int):
    while not(liste_chaine.est_vide()) and n > 0:
        liste_chaine = liste_chaine.queue()
        n = n-1
    return liste_chaine.tete()
    
    
    
if __name__ == '__main__':
    L = Liste()
    L.inserer(3)
    L.inserer(7)
    L.inserer(4)
    lg = longueur(L)
    print(lg,L)
    print(atteint(L,0))