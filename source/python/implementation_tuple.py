def creer_liste():
    return ()

def est_vide(liste):
    return liste == ()

def inserer(element, liste):
    return (element, liste)

def tete(liste):
    assert not est_vide(liste), "tête, liste vide !"
    element, _ = liste
    return element

def queue(liste):
    assert not est_vide(liste), "queue, liste vide !"
    _, queue = liste
    return queue
