Exercices
===========

.. note::

    On donne l'interface d'une liste chainée qui sera utilisée dans les exercices.

    -   Le constructeur ``creer_liste()`` qui crée une liste chainée vide, c'est à dire un tuple vide;
    -   L'opérateur ``inserer(element, liste)`` qui ajoute un élément en tête de la liste chainée;
    -   Les accesseurs ``tete(liste)`` qui renvoie la tête de la liste chainée sans le supprimer et ``queue(liste)`` qui renvoie la liste chainée sans son premier élément;
    -   L'accesseur ``est_vide(liste)`` qui teste si la liste chainée est vide.

.. exercice::

    On considère la liste chainée représentée ci-dessous:

    .. figure:: ../img/liste_chainee_exemple.svg
        :align: center
        :width: 360px
   

    Cette liste chainée est constituée de trois maillons repésentés par des rectangles. Chaque maillon se compose de 2 parties:

    -   la tête qui contient une valeur;
    -   la queue qui contient la suite de la liste.

    Pour schématiser cette liste, on pourra la noter ``L->[1]->[2]->[4]->[]``.

    #.  On construit cette liste chainée L en écrivant chaque maillon sous la forme d'un tuple (tête, queue). 

        a.  Écrire avec des tuples cette liste chainée L.
        b.  Donner une suite d'instructions en Python qui permet de construire cette liste chainée L. On n'utilise que les fonctions de l'interface de la liste chainée.

    #.  Comment mémoriser dans une variable Q la liste chainée ``[2]->[4]->[]`` à partir de la liste chainée L ?
    #.  On construit une liste chainée P en saisissant les instructions Python suivantes dans une console:

        >>> P = creer_liste()
        >>> P = inserer(tete(L),P)
        >>> P = inserer(tete(queue(L)),P)

        Représenter le contenu de la liste chainée P.

    #.  On construit la liste chainée R représentée par ``[1]->[2]->[]``. Donner les instructions Python qui permettent de construire R à partir de la liste chainée L ?

.. exercice::

    #.  On donne la représentation d'une liste chainée:

        .. image:: ../img/liste_chainee_1.svg
            :align: center
            :width: 420px

        Donner la suite d'instruction en Python pour créer cette liste chainée.

    #.  En utilisant la liste ``L1``, créer les différentes listes  de l'illustration ci-dessous.

        .. image:: ../img/liste_chainee_2.svg
            :align: center
            :width: 420px

.. exercice::

    On donne une implémentation de la liste chainée avec des tuples.

    .. literalinclude:: ../python/implementation_tuple.py

    #.  Créer et afficher la liste ``L1`` ci-dessous:

        .. image:: ../img/liste_chainee_1.svg
            :align: center
            :width: 420px
            
    #.  On souhaite créer une fonction ``afficher(liste)`` qui prend en paramètre une liste et affiche la liste sous forme de chaine:
    
        -   chaque valeur sera écrite entre crochets
        -   les valeurs seront reliées par des flèches "->".
    
        Voici le début du code de la fonction à compléter:

        .. code:: python

            def afficher(liste):
                chaine = ""
                while not est_vide(liste):
                    t, liste = ...
                    chaine += "[" + ... + "]->"
                chaine += ...
                return ...

.. exercice::

    On souhaite ajouter quelques fonctions pour agir sur une liste chainée.

    #.  La fonction ``longueur`` prend en paramètre une liste et renvoie le nombre d'éléments de la liste. Coder cette fonction sachant que si la liste est vide, la longueur est égale à 0.
    #.  La fonction ``atteint`` prend en paramètres une liste et un nombre entier positif. La fonction renvoie le nombre de la liste situé à la position indiquée par le nombre entier saisi en argument. On gèrera le cas ou la position est supérieure à la longueur de la liste pour éviter une erreur. La tête de la liste a pour position 0. Coder en Python la fonction.

.. exercice::

    Soit L une liste chainée qui contient les valeurs ``Bob``, ``Alice``, ``Patrick``, ``Gary`` et ``Carlo``. On considère que le nom ``Bob`` est la tête de la liste et que l'ordre est respecté.

    #.  Créer en Python cette liste chainée.
    #.  La fonction ``renverse`` prend en paramètre une liste et renverse les valeurs de la liste. La tête de liste devient la dernière valeur de la liste. La fonction renvoie une liste chainée.
    
        a.  Coder la fonction ``renverse``.
        b.  Créer la liste chainée K en renversant la liste L.
    
    3.  La fonction ``inserer_fin`` prend en paramètre une liste et une valeur à insérer en fin de liste. La fonction renvoie la liste chainée avec la valeur insérée en fin de liste. On peut utiliser l'algorithme suivant pour notre fonction:

        .. code:: text
            
            1. créer une liste tmp contenant la valeur à insérer
            2. renverser la liste qui doit accueillir la nouvelle valeur
            3. insérer les éléments de la liste renversée dans la liste tmp.

        Coder la fonction et insérer une nouvelle valeur en fin de liste.
