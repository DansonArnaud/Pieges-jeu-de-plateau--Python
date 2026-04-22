from fltk import *
from random import randint
import math


def dessiner_plateau(pas):
    """
    Dessine un plateau avec des cases grises au centre et une bordure bisque.

    Args:
        pas (int): La taille d'une case sur le plateau.
    """
    x = 0
    y = 0
    for ligne in range(11):
        for colonne in range(11):
            if colonne > 1 and colonne < 9 and ligne > 1 and ligne < 9:
                rectangle(x, y, x + pas, y + pas, epaisseur=5, couleur="bisque", remplissage="grey")
            x += pas
        x = 0
        y += pas


def trou(fus, pas, pas_2):
    """
    Dessine les cercles représentant les trous.

    Args:
        fus (list): Matrice représentant l'emplacement des trous.
        pas (int): Taille d'une case.
        pas_2 (int): Taille d'une demi-case.
    """
    for i in range(7):
        for j in range(7):
            if fus[i][j] == "O":
                cercle(pas_2 * 5 + pas_2 * j * 2, pas_2 * 5 + pas_2 * i * 2, pas_2 - 2.5, "orange", "orange")
            elif fus[i][j] == "B":
                cercle(pas_2 * 5 + pas_2 * j * 2, pas_2 * 5 + pas_2 * i * 2, pas_2 - 2.5, "white", "white")
            else:
                cercle(pas_2 * 5 + pas_2 * j * 2, pas_2 * 5 + pas_2 * i * 2, pas_2 - 2.5, "black", "black")


def tiret_verticale(lst_verticale, pas, b):
    """
    Dessine les tirettes verticales.

    Args:
        lst_verticale (list): Présence des tirettes verticales.
        pas (int): Taille d'une case.
        b (int): Largeur des tirettes.
    """
    for i in range(7):
        if lst_verticale[i] == 0:
            rectangle(pas * 2 + pas * i, b * 11, pas * 2 + pas * (i + 1), b * 12, "orange", "orange")
            rectangle(pas * 2 + pas * i, pas * 11 - b, pas * 2 + pas * (i + 1), pas * 11, "orange", "orange")
            rectangle(pas * 2 + pas * i + b * 3 - b / 2, pas * 9 + 2.5, pas * 2 + pas * i + b * 3 + b / 2, pas * 11 - b, "orange", "orange")
        elif lst_verticale[i] == 1:
            rectangle(pas * 2 + pas * i, b * 5 + b / 2, pas * 2 + pas * (i + 1), b * 6 + b / 2, "orange", "orange")
            rectangle(pas * 2 + pas * i + b * 3 - b / 2, pas + b / 2, pas * 2 + pas * i + b * 3 + b / 2, pas * 2 - 2.5, "orange", "orange")
            rectangle(pas * 2 + pas * i + b * 3 - b / 2, pas * 9 + 2.5, pas * 2 + pas * i + b * 3 + b / 2, pas * 10 - b / 2, "orange", "orange")
            rectangle(pas * 2 + pas * i, pas * 10 - b / 2, pas * 2 + pas * (i + 1), pas * 10 + b / 2, "orange", "orange")
        elif lst_verticale[i] == 2:
            rectangle(pas * 2 + pas * i, 0, pas * 2 + pas * (i + 1), b, "orange", "orange")
            rectangle(pas * 2 + pas * i + b * 3 - b / 2, b, pas * 2 + pas * i + b * 3 + b / 2, pas * 2 - 2.5, "orange", "orange")
            rectangle(pas * 2 + pas * i, pas * 9, pas * 2 + pas * (i + 1), pas * 9 + b, "orange", "orange")


def tiret_horizontale(lst_horizontale, pas, b):
    """
    Dessine les tirettes horizontales.

    Args:
        lst_horizontale (list): Présence des tirettes horizontales.
        pas (int): Taille d'une case.
        b (int): Largeur des tirettes.
    """
    for i in range(7):
        if lst_horizontale[i] == 0:
            rectangle(pas * 2 - b, pas * 2 + pas * i, pas * 2, pas * 3 + pas * i, "white", "white")
            rectangle(pas * 9 + 2.5, pas * 2 + pas * i + b * 3 - b / 2, pas * 11 - b, pas * 2 + pas * i + b * 3 + b / 2, "white", "white")
            rectangle(pas * 11 - b, pas * 2 + pas * i, pas * 11, pas * 3 + pas * i, "white", "white")
        elif lst_horizontale[i] == 1:
            rectangle(pas - b / 2, pas * 2 + pas * i, pas + b / 2, pas * 3 + pas * i, "white", "white")
            rectangle(pas + b / 2, pas * 2 + pas * i + b * 3 - b / 2, pas * 2 - 2.5, pas * 2 + pas * i + b * 3 + b / 2, "white", "white")
            rectangle(pas * 9 + 2.5, pas * 2 + pas * i + b * 3 - b / 2, pas * 10 - b / 2, pas * 2 + pas * i + b * 3 + b / 2, "white", "white")
            rectangle(pas * 10 - b / 2, pas * 2 + pas * i, pas * 10 + b / 2, pas * 3 + pas * i, "white", "white")
        elif lst_horizontale[i] == 2:
            rectangle(0, pas * 2 + pas * i, b, pas * 3 + pas * i, "white", "white")
            rectangle(b, pas * 2 + pas * i + b * 3 - b / 2, pas * 2 - 2.5, pas * 2 + pas * i + b * 3 + b / 2, "white", "white")
            rectangle(pas * 9, pas * 2 + pas * i, pas * 9 + b, pas * 3 + pas * i, "white", "white")


def bille(position_billes, pas, lst_couleur):
    """
    Dessine les billes sur la grille.

    Args:
        position_billes (list): Configuration des billes.
        pas (int): Taille d'une case.
        lst_couleur (list): Couleurs des joueurs.
    """
    for i in range(7):
        for j in range(7):
            val = position_billes[i][j]
            if val.startswith("bille"):
                idx = int(val[-1])
                couleur_bille = lst_couleur[idx]
                cercle(
                    pas * 2 + pas * j + pas / 2,
                    pas * 2 + pas * i + pas / 2,
                    pas / 4,
                    couleur_bille,
                    couleur_bille
                )


def dessin(taille_fenetre, zoom, pas, pas_2, b, fus, lst_verticale, lst_horizontale, position_billes, lst_couleur):
    """
    Dessine l'ensemble du plateau de jeu.

    Args:
        taille_fenetre (int): Taille de la fenêtre.
        zoom (int): Zoom appliqué à l'image de fond.
        pas (float): Taille d'une case.
        pas_2 (float): Taille d'une demi-case.
        b (float): Largeur des tirettes.
        fus (list): Grille fusionnée.
        lst_verticale (list): Positions des tirettes verticales.
        lst_horizontale (list): Positions des tirettes horizontales.
        position_billes (list): Positions des billes.
        lst_couleur (list): Couleurs des joueurs.
    """
    image(taille_fenetre / 2, taille_fenetre / 2, "bois4.ppm",
          largeur=taille_fenetre + zoom, hauteur=taille_fenetre + zoom, ancrage='center', tag='im')
    rectangle(0, 0, taille_fenetre, taille_fenetre, epaisseur=10, couleur="burlywood")
    dessiner_plateau(pas)
    trou(fus, pas, pas_2)
    tiret_verticale(lst_verticale, pas, b)
    tiret_horizontale(lst_horizontale, pas, b)
    bille(position_billes, pas, lst_couleur)


def creer_grille_horizontale():
    """
    Génère une grille horizontale avec des tirets et des trous aléatoires.

    Returns:
        list: Grille horizontale générée.
    """
    lst = [["B"] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if j % 3 == 2:
                lst[i][j] = "T"
    for i in range(9):
        ale = randint(0, 9)
        for _ in range(ale):
            position_trou = randint(0, 8)
            lst[i][position_trou] = "T"
    return lst


def creer_grille_verticale():
    """
    Génère une grille verticale avec des tirets et des trous aléatoires.

    Returns:
        list: Grille verticale générée.
    """
    lst = [["O"] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if j % 3 == 2:
                lst[j][i] = "T"
    for i in range(9):
        ale = randint(1, 9)
        for _ in range(ale):
            ligne_avec_O = randint(0, 8)
            lst[ligne_avec_O][i] = "T"
    return lst


def melanger(grille_v, grille_h, lst_verticale, lst_horizontale):
    """
    Décale aléatoirement les grilles et met à jour les listes de tirettes.

    Args:
        grille_v (list): Grille verticale.
        grille_h (list): Grille horizontale.
        lst_verticale (list): Liste des positions verticales.
        lst_horizontale (list): Liste des positions horizontales.
    """
    for i in range(9):
        a = randint(0, 2)
        b_val = randint(0, 2)
        if i < 7:
            lst_verticale[i] = a
            lst_horizontale[i] = b_val
        for _ in range(a):
            verticale(grille_v, "h", i)
        for _ in range(b_val):
            horizontale(grille_h, "g", i)


def calculer_position_billes(fus, nb_j):
    """
    Positionne les billes sur le plateau selon le nombre de joueurs.

    Args:
        fus (list): Grille fusionnée.
        nb_j (int): Nombre de joueurs.

    Returns:
        list: Position des billes.
    """
    if nb_j == 1:
        nb_billes = 0
        lst = [[""] * 7 for _ in range(7)]
        while nb_billes != 14:
            i_bille = randint(0, 6)
            j_bille = randint(0, 6)
            if fus[i_bille][j_bille] != "T" and lst[i_bille][j_bille] == "":
                lst[i_bille][j_bille] = "bille0"
                nb_billes += 1
        return lst
    else:
        return [[""] * 7 for _ in range(7)]


def verticale(grille, direction, colonne):
    """
    Déplace les éléments d'une colonne vers le haut ou le bas.

    Args:
        grille (list): La grille à modifier.
        direction (str): "b" pour bas, "h" pour haut.
        colonne (int): Index de la colonne.

    Returns:
        list: La grille modifiée.

    Doctests:
    >>> grille = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    >>> verticale(grille, "h", 1)
    [[1, 5, 3], [4, 8, 6], [7, 2, 9]]
    """
    taille = len(grille)
    dernier = grille[-1][colonne]
    premier = grille[0][colonne]
    if direction == "b":
        for i in range(taille - 1, 0, -1):
            grille[i][colonne] = grille[i - 1][colonne]
        grille[0][colonne] = dernier
    elif direction == "h":
        for i in range(taille - 1):
            grille[i][colonne] = grille[i + 1][colonne]
        grille[-1][colonne] = premier
    return grille


def horizontale(grille, direction, ligne):
    """
    Déplace les éléments d'une ligne vers la gauche ou la droite.

    Args:
        grille (list): La grille à modifier.
        direction (str): "g" pour gauche, "d" pour droite.
        ligne (int): Index de la ligne.

    Returns:
        list: La grille modifiée.

    Doctests:
    >>> grille = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    >>> horizontale(grille, "d", 1)
    [[1, 2, 3], [6, 4, 5], [7, 8, 9]]
    """
    taille = len(grille[ligne])
    dernier = grille[ligne][-1]
    premier = grille[ligne][0]
    if direction == "d":
        for i in range(taille - 1, 0, -1):
            grille[ligne][i] = grille[ligne][i - 1]
        grille[ligne][0] = dernier
    elif direction == "g":
        for i in range(taille - 1):
            grille[ligne][i] = grille[ligne][i + 1]
        grille[ligne][-1] = premier
    return grille


def fusion(grille_v, grille_h):
    """
    Fusionne la grille verticale avec la grille horizontale.

    Args:
        grille_v (list): Grille verticale.
        grille_h (list): Grille horizontale.

    Returns:
        list: Grille fusionnée (7x7).
    """
    fus = [[""] * 7 for _ in range(7)]
    for i in range(7):
        for j in range(7):
            if grille_v[i][j] == "O" and grille_h[i][j] == "T":
                fus[i][j] = "O"
            elif grille_v[i][j] == "T" and grille_h[i][j] == "T":
                fus[i][j] = "T"
            else:
                fus[i][j] = "B"
    return fus


def verifie(fus, position_billes):
    """
    Retire les billes tombées dans un trou.

    Args:
        fus (list): Grille fusionnée.
        position_billes (list): Positions des billes.

    Returns:
        list: Positions mises à jour.
    """
    for i in range(len(position_billes)):
        for j in range(len(position_billes[i])):
            if fus[i][j] == "T":
                position_billes[i][j] = ""
    return position_billes


def victoire(nb_j, position_billes, nb_coup, taille_fenetre, pas, pas_2):
    """
    Vérifie s'il y a une victoire.

    Args:
        nb_j (int): Nombre de joueurs.
        position_billes (list): Positions des billes.
        nb_coup (int): Nombre de coups effectués.
        taille_fenetre (int): Taille de la fenêtre.
        pas (float): Taille d'une case.
        pas_2 (float): Taille d'une demi-case.

    Returns:
        bool: True si la partie continue, False si elle est terminée.
    """
    if nb_j == 1:
        for x in range(len(position_billes)):
            for y in range(len(position_billes[x])):
                if position_billes[x][y] != "":
                    return True
        texte(taille_fenetre / 2, taille_fenetre / 8,
              "Bravo, vous avez réussi en " + str(nb_coup) + " coups",
              couleur="black", taille=int(30 * (taille_fenetre / 650)), ancrage='center')
        attente(3)
        return False
    else:
        bille_ref = ""
        for x in range(len(position_billes)):
            for y in range(len(position_billes[x])):
                if position_billes[x][y] != "":
                    bille_ref = position_billes[x][y]
                    break
            if bille_ref:
                break

        if bille_ref == "":
            texte(taille_fenetre / 2, taille_fenetre / 8,
                  "Tout le monde a perdu",
                  couleur="white", taille=int(30 * (taille_fenetre / 650)), ancrage='center')
            attente(3)
            return False

        for x in range(len(position_billes)):
            for y in range(len(position_billes[x])):
                val = position_billes[x][y]
                if val != "" and val != bille_ref:
                    return True

        j = int(bille_ref[-1]) + 1
        texte(taille_fenetre / 2, pas_2, "Bravo",
              couleur="white", taille=int(24 * (taille_fenetre / 650)), ancrage='center')
        texte(taille_fenetre / 2, pas_2 * 3,
              "Joueur " + str(j) + " est le gagnant",
              couleur="white", taille=int(24 * (taille_fenetre / 650)), ancrage='center')
        attente(3)
        return False


def initi(nb_j, position_billes, fus, taille_fenetre, pas):
    """
    Permet à chaque joueur de placer ses billes en cliquant sur le plateau.

    Args:
        nb_j (int): Nombre de joueurs.
        position_billes (list): Positions initiales des billes.
        fus (list): Grille fusionnée.
        taille_fenetre (int): Taille de la fenêtre.
        pas (float): Taille d'une case.

    Returns:
        list: Positions des billes après l'initialisation.
    """
    texte(taille_fenetre/2, pas/2, "Placez vos billes ", couleur="tomato", taille=int(24*(taille_fenetre/650)), ancrage='center', tag='A')
    d = 0
    for i in range (5) :
        c = 0
        while c < nb_j :
            if d == 0 :
                texte(taille_fenetre/2, pas/2 + pas, "Joueur " + str(c+1) + ": bille "+ str(i+1)+ "/5", couleur="white", taille=int(24*(taille_fenetre/650)), ancrage='center', tag='B')
                d += 1
            mise_a_jour()
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'ClicGauche':
                a = int(ordonnee(ev)//(taille_fenetre/11)-2)
                b = int(abscisse(ev)//(taille_fenetre/11)-2)
                if a>=0 and b>=0 and a<=6 and b<=6 :
                    if fus[a][b] != "T" :
                        if position_billes[a][b] == "":
                            position_billes[a][b] = "bille" + str(c)
                            bille(position_billes, pas, lst_couleur)
                            if ev != None :
                                c += 1
                                d = 0
                                efface("B")
                        else :
                            texte(taille_fenetre/2, taille_fenetre/2, "Joueur " + str(c+1) + " on peux pas mettre de bille ici, y'a déjà une bille", couleur="red", taille=int(19*(taille_fenetre/650)), ancrage='center', tag='C')
                            attente(1)
                            efface("C")
                    else :
                        texte(taille_fenetre/2, taille_fenetre/2, "Joueur " + str(c+1) + " on peux pas mettre de bille ici, c'est un trou", couleur="red", taille=int(19*(taille_fenetre/650)), ancrage='center', tag='C')
                        attente(1)
                        efface("C")
                else :
                    texte(taille_fenetre/2, taille_fenetre/2,"Joueur " + str(c+1) + " on peux pas mettre de bille ici, c'est hors du plateau", couleur="red", taille=int(17*(taille_fenetre/650)), ancrage='center', tag='C')
                    attente(1)
                    efface("C")
            elif ty == 'Quitte':  
                exit()
    efface("A")
    mise_a_jour()
    return position_billes


def mouv(grille_v, grille_h, lst_verticale, lst_horizontale, j_actuel, taille_fenetre, pas):
    """
    Gère le déplacement des tirettes en réponse aux clics.

    Args:
        grille_v (list): Grille verticale.
        grille_h (list): Grille horizontale.
        lst_verticale (list): Positions des tirettes verticales.
        lst_horizontale (list): Positions des tirettes horizontales.
        j_actuel (int): Index du joueur actuel.
        taille_fenetre (int): Taille de la fenêtre.
        pas (float): Taille d'une case.
    """
    cond = True
    while cond:
        mise_a_jour()
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'ClicGauche':
            a = ordonnee(ev)
            b = abscisse(ev)
            c = int(a // (taille_fenetre / 11) - 2)
            d = int(b // (taille_fenetre / 11) - 2)

            msg_max = "Joueur " + str(j_actuel + 1) + " : la tirette est au maximum"
            msg_invalid = "Joueur " + str(j_actuel + 1) + " : aucune tirette ici"

            if a < pas * 2 and 0 <= d <= 6:
                if lst_verticale[d] < 2:
                    verticale(grille_v, "h", d)
                    lst_verticale[d] += 1
                    cond = False
                else:
                    texte(taille_fenetre / 2, taille_fenetre / 2, msg_max,
                          couleur="red", taille=int(17 * (taille_fenetre / 650)), ancrage='center', tag='C')
                    attente(1)
                    efface("C")
            elif a > pas * 9 and 0 <= d <= 6:
                if lst_verticale[d] > 0:
                    verticale(grille_v, "b", d)
                    lst_verticale[d] -= 1
                    cond = False
                else:
                    texte(taille_fenetre / 2, taille_fenetre / 2, msg_max,
                          couleur="red", taille=int(17 * (taille_fenetre / 650)), ancrage='center', tag='C')
                    attente(1)
                    efface("C")
            elif b < pas * 2 and 0 <= c <= 6:
                if lst_horizontale[c] < 2:
                    horizontale(grille_h, "g", c)
                    lst_horizontale[c] += 1
                    cond = False
                else:
                    texte(taille_fenetre / 2, taille_fenetre / 2, msg_max,
                          couleur="red", taille=int(17 * (taille_fenetre / 650)), ancrage='center', tag='C')
                    attente(1)
                    efface("C")
            elif b > pas * 9 and 0 <= c <= 6:
                if lst_horizontale[c] > 0:
                    horizontale(grille_h, "d", c)
                    lst_horizontale[c] -= 1
                    cond = False
                else:
                    texte(taille_fenetre / 2, taille_fenetre / 2, msg_max,
                          couleur="red", taille=int(17 * (taille_fenetre / 650)), ancrage='center', tag='C')
                    attente(1)
                    efface("C")
            elif pas * 9 < b < taille_fenetre and 0 < a < pas * 2:
                return True  
            else:
                texte(taille_fenetre / 2, taille_fenetre / 2, msg_invalid,
                      couleur="red", taille=int(17 * (taille_fenetre / 650)), ancrage='center', tag='C')
                attente(1)
                efface("C")
        elif ty == 'Quitte':
            exit()


def cercle_ovale(centre, rayon_x, rayon_y, nb_points=100):
    """
    Génère les coordonnées d'une ellipse.

    Args:
        centre (tuple): Coordonnées du centre.
        rayon_x (float): Rayon horizontal.
        rayon_y (float): Rayon vertical.
        nb_points (int): Nombre de points (défaut 100).

    Returns:
        list: Coordonnées de l'ellipse.
    """
    coords = []
    for i in range(nb_points):
        angle = 2 * math.pi * i / nb_points
        x = centre[0] + rayon_x * math.cos(angle)
        y = centre[1] + rayon_y * math.sin(angle)
        coords.append((x, y))
    return coords


def joueur(taille_fenetre, pas, pas_2):
    """
    Permet de choisir le nombre de joueurs.

    Args:
        taille_fenetre (int): Taille de la fenêtre.
        pas (float): Taille d'une case.
        pas_2 (float): Taille d'une demi-case.

    Returns:
        int: Nombre de joueurs sélectionné.
    """
    x = 4
    for i in range(2):
        rectangle(pas * (2 + i * x), pas * 3, pas * (5 + i * x), pas * 5, epaisseur=3, couleur="black")
        texte(pas * (3 + i * x) + pas_2, pas * 4, str(i + 1) + " joueur",
              couleur="black", taille=int(24 * (taille_fenetre / 650)), ancrage='center')
        coord = cercle_ovale((pas * (3 + i * x) + pas_2, pas * 4), pas * 1.5, pas, nb_points=100)
        polygone(coord, couleur="black", epaisseur=4)

        rectangle(pas * (2 + i * x), pas * 6, pas * (5 + i * x), pas * 8, epaisseur=3, couleur="black")
        texte(pas * (3 + i * x) + pas_2, pas * 7, str(i + 3) + " joueur",
              couleur="black", taille=int(24 * (taille_fenetre / 650)), ancrage='center')
        coord = cercle_ovale((pas * (3 + i * x) + pas_2, pas * 7), pas * 1.5, pas, nb_points=100)
        polygone(coord, couleur="black", epaisseur=4)

    texte(taille_fenetre / 2, taille_fenetre / 8, "Nombre de joueurs ?",
          couleur="black", taille=int(24 * (taille_fenetre / 650)), ancrage='center')

    while True:
        mise_a_jour()
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'ClicGauche':
            c = ordonnee(ev)
            d = abscisse(ev)
            if pas * 2 <= d <= pas * 5 and pas * 3 <= c <= pas * 5:
                return 1
            elif pas * 6 <= d <= pas * 9 and pas * 3 <= c <= pas * 5:
                return 2
            elif pas * 2 <= d <= pas * 5 and pas * 6 <= c <= pas * 8:
                return 3
            elif pas * 6 <= d <= pas * 9 and pas * 6 <= c <= pas * 8:
                return 4
            else:
                texte(taille_fenetre / 2, taille_fenetre / 2, "Cliquez dans les rectangles",
                      couleur="red", taille=int(19 * (taille_fenetre / 650)), ancrage='center', tag='C')
                attente(1)
                efface("C")
        elif ty == 'Quitte':
            exit()


def couleur(nb_j, taille_fenetre, pas):
    """
    Permet aux joueurs de choisir leur couleur.

    Args:
        nb_j (int): Nombre de joueurs.
        taille_fenetre (int): Taille de la fenêtre.
        pas (float): Taille d'une case.

    Returns:
        list: Couleurs choisies par les joueurs.
    """
    x = 4
    lst_couleur = []
    for i in range(2):
        rectangle(pas * (2 + i * x), pas * 3, pas * (5 + i * x), pas * 5,
                  epaisseur=3, couleur="black", remplissage="pink")
        rectangle(pas * 6, pas * 3, pas * 9, pas * 5,
                  epaisseur=3, couleur="black", remplissage="blue")
        rectangle(pas * (2 + i * x), pas * 6, pas * (5 + i * x), pas * 8,
                  epaisseur=3, couleur="black", remplissage="yellow")
        rectangle(pas * 6, pas * 6, pas * 9, pas * 8,
                  epaisseur=3, couleur="black", remplissage="green")

    couleurs_disponibles = {
        (pas * 2, pas * 3, pas * 5, pas * 5): "pink",
        (pas * 6, pas * 3, pas * 9, pas * 5): "blue",
        (pas * 2, pas * 6, pas * 5, pas * 8): "yellow",
        (pas * 6, pas * 6, pas * 9, pas * 8): "green",
    }

    noms_couleurs = {
        "pink": "rose",
        "blue": "bleu",
        "yellow": "jaune",
        "green": "vert",
    }

    for i in range(nb_j):
        cond = True
        texte(taille_fenetre / 2, taille_fenetre / 8,
              "Joueur " + str(i + 1) + " : choisis ta couleur",
              couleur="black", police="Georgia", taille=int(24 * (taille_fenetre / 650)), ancrage='center', tag='C')
        while cond:
            mise_a_jour()
            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'ClicGauche':
                c = ordonnee(ev)
                d = abscisse(ev)
                choix = None
                for (x1, y1, x2, y2), nom in couleurs_disponibles.items():
                    if x1 <= d <= x2 and y1 <= c <= y2:
                        choix = nom
                        break
                if choix:
                    if choix not in lst_couleur:
                        lst_couleur.append(choix)
                        cond = False
                        efface("C")
                    else:
                        texte(taille_fenetre / 2, taille_fenetre / 2,
                              "La couleur " + noms_couleurs[choix] + " est déjà prise",
                              couleur="red", taille=int(19 * (taille_fenetre / 650)), ancrage='center', tag='A')
                        attente(1)
                        efface("A")
                else:
                    texte(taille_fenetre / 2, taille_fenetre / 2, "Cliquez dans les rectangles",
                          couleur="red", taille=int(19 * (taille_fenetre / 650)), ancrage='center', tag='C')
                    attente(1)
                    efface("C")
            elif ty == 'Quitte':
                exit()
    return lst_couleur


if __name__ == '__main__':
    taille_fenetre = 600
    zoom = taille_fenetre - 200
    pas = taille_fenetre / 11
    pas_2 = taille_fenetre / 22
    b = pas / 6

    cree_fenetre(taille_fenetre, taille_fenetre)
    
    while True:
        image(taille_fenetre / 2, taille_fenetre / 2, "bois-2.ppm",
              largeur=taille_fenetre + zoom, hauteur=taille_fenetre + zoom, ancrage='center', tag='im')
        rectangle(0, 0, taille_fenetre, taille_fenetre, epaisseur=10, couleur="burlywood")
        rectangle((pas * 2) - 5, (pas * 2) - 5, pas * 9 + 5, pas * 9 + 5, epaisseur=10, couleur="saddlebrown")

        nb_j = joueur(taille_fenetre, pas, pas_2)
        efface_tout()

        image(taille_fenetre / 2, taille_fenetre / 2, "bois-2.ppm",
              largeur=taille_fenetre + zoom, hauteur=taille_fenetre + zoom, ancrage='center', tag='im')
        rectangle(0, 0, taille_fenetre, taille_fenetre, epaisseur=10, couleur="burlywood")

        lst_couleur = couleur(nb_j, taille_fenetre, pas)
        efface_tout()

        lst_verticale = [0] * 7
        lst_horizontale = [0] * 7

        grille_v = creer_grille_verticale()
        grille_h = creer_grille_horizontale()
        melanger(grille_v, grille_h, lst_verticale, lst_horizontale)
        fus = fusion(grille_v, grille_h)

        pos_billes = calculer_position_billes(fus, nb_j)

        dessin(taille_fenetre, zoom, pas, pas_2, b, fus, lst_verticale, lst_horizontale, pos_billes, lst_couleur)

        j_actuel = 0
        nb_coup = 0

        if nb_j > 1:
            pos_billes = initi(nb_j, pos_billes, fus, taille_fenetre, pas)

        while victoire(nb_j, pos_billes, nb_coup, taille_fenetre, pas, pas_2):
            texte(5, pas / 2, "Tour du joueur " + str(j_actuel + 1), couleur="white", taille=int(14 * (taille_fenetre / 650)), ancrage='nw')
            texte(pas* 10, pas, "Menu", "black", "center")
            test = mouv(grille_v, grille_h, lst_verticale, lst_horizontale, j_actuel, taille_fenetre, pas)
            if test :
                break 
            j_actuel = (j_actuel + 1) % nb_j
            fus = fusion(grille_v, grille_h)
            verifie(fus, pos_billes)
            efface_tout()
            image(taille_fenetre / 2, taille_fenetre / 2, "bois4.ppm", largeur=taille_fenetre + zoom, hauteur=taille_fenetre + zoom, ancrage='center', tag='im')
            rectangle(0, 0, taille_fenetre, taille_fenetre, epaisseur=10, couleur="burlywood")
            dessin(taille_fenetre, zoom, pas, pas_2, b, fus, lst_verticale, lst_horizontale, pos_billes, lst_couleur)
            nb_coup += 1
        
        if not test:
            attend_ev()
            efface_tout()
