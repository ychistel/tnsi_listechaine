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

if __name__ == '__main__':
    L = creer_liste()
    L = inserer(4,L)
    L = inserer(2,L)
    L = inserer(1,L)
    print(L)
    P = creer_liste()
    P = inserer(tete(L),P)
    P = inserer(tete(queue(L)),P)
    print(P)
    Q = queue(L)
    print(Q)
    R = creer_liste()
    R = inserer(tete(queue(L)),R)
    R = inserer(tete(L),R)
    print(R)