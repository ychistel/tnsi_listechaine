class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return "["+str(self.valeur)+"]->" + "[]"
        else:
            return "["+str(self.va