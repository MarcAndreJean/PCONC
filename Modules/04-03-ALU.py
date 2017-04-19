#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-03-ALU.py

    Identification  : 04-03-ALU
    Titre           : ALU
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 15-04-2017
    Description     : ALU du micro-ordinateur.


    Le module ``ALU``
    ================================

    Ce module contient la classe ALU qui représente l'unité arithmétique
    du processeur. Il s'agit d'une sous-composante du processeur.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Verification"


class ALU:
    """
        class ALU
        ========================

        Cette classe est la représentation de l'unité ALU du processeur.
        Elle s'occupe de retourner le résultat de toutes les opérations
        arithmétiques et de comparaisons. Soit:
        - Arithmétique:
            - ADD (addition A + B)
            - SUB (soustraction A - B)
            - MUL (multiplication A * B)
            - DIV (division A / B)
        - Comparaisons:
            - OR (bitwise A or B)
            - AND (bitwise A and B)
            - XOR (bitwise A xor B)
            - NOT (bitwise not A)
            - LT (Vrai si A plus petit que B)
            - GT (Vrai si A plus grand que B)
            - LE (Vrai si A plus petit ou égal à B)
            - GE (Vrai si A plus grand ou égal à B)
            - EQ (Vrai si A est égal à B)
            - EZ (Vrai si A est égal à Zéro)
            - NZ (Vrai si A N'est PAS égal à Zéro)


    """

    def __init__(self):
        """
            Constructeur de la classe ALU.

            Le constructeur initialise l'obet de la classe ALU.

        """
        return

    def fonctionADD(self, val1, val2):
        """
            Fonction qui additionne deux valeurs ensemble.

            Cette fonction permet de retourner la somme de val1 et val2.

            :example:
            >>> fonctionADD(1,2)
            3

            :param val1: Nombre entier de gauche de l'addition.
            :type val1: int
            :param val2: Nombre entier de droite de l'addition.
            :type val2: int

            :return: Résultat de l'addition entre val1 et val2.
            :rtype: int

        """
        return val1 + val2

    def fonctionSUB(self, val1, val2):
        """
            Fonction qui soustrait deux valeurs ensemble.

            Cette fonction permet de retourner la difference de val1 et
            val2.

            :example:
            >>> fonctionSUB(2, 1)
            1

            :param val1: Nombre entier de gauche de la soustraction.
            :type val1: int
            :param val2: Nombre entier de droite de la soustraction.
            :type val2: int

            :return: Résultat de la soustraction entre val1 et val2.
            :rtype: int

        """
        return val1 - val2

    def fonctionMUL(self, val1, val2):
        """
            Fonction qui multiplie deux valeurs ensemble.

            Cette fonction permet de retourner le résultat de la
            multiplication de val1 par val2.

            :example:
            >>> fonctionMUL(2, 2)
            4

            :param val1: Nombre entier de gauche de la multiplication.
            :type val1: int
            :param val2: Nombre entier de droite de la multiplication.
            :type val2: int

            :return: Résultat de la multiplication entre val1 et val2.
            :rtype: int

        """
        return val1 * val2

    def fonctionDIV(self, val1, val2):
        """
            Fonction qui divise deux valeurs ensemble.

            Cette fonction permet de retourner le résultat de la division
            entière de val1 par val2.

            :example:
            >>> fonctionDIV(1, 3)
            0
            >>> fonctionDIV(4, 2)
            2
            >>> fonctionDIV(16, 2)
            8

            :param val1: Nombre entier de gauche de la division.
            :type val1: int
            :param val2: Nombre entier de droite de la division.
            :type val2: int

            :return: Résultat de la division entre val1 et val2.
            :rtype: int

        """
        # Gestion division par zéro.
        if val2 == 0:
            return 0
        # Division entière.
        return int(val1 // val2)

    def fonctionOR(self, val1, val2):
        """
            Fonction qui effectue un OR bitwise entre deux valeurs.

            Cette fonction permet de retourner le résultat d'un OR
            logique entre deux valeurs val1 et val2.

            :example:
            >>> fonctionOR(1, 1)
            1
            >>> fonctionOR(0, 1)
            1
            >>> fonctionOR(0, 0)
            0
            >>> fonctionOR(0xAFAF, 0xFAFA)
            0xFFFF

            :param val1: Nombre entier de gauche du OR logique.
            :type val1: int
            :param val2: Nombre entier de droite du OR logique.
            :type val2: int

            :return: Résultat du OR logique entre val1 et val2.
            :rtype: int

        """
        return val1 | val2

    def fonctionAND(self, val1, val2):
        """
            Fonction qui effectue un AND bitwise entre deux valeurs.

            Cette fonction permet de retourner le résultat d'un AND
            logique entre deux valeurs val1 et val2.

            :example:
            >>> fonctionAND(1, 1)
            1
            >>> fonctionAND(0, 1)
            0
            >>> fonctionAND(0, 0)
            0
            >>> fonctionAND(0xAFAF, 0xFAFA)
            0xFFFF

            :param val1: Nombre entier de gauche du AND logique.
            :type val1: int
            :param val2: Nombre entier de droite du AND logique.
            :type val2: int

            :return: Résultat du AND logique entre val1 et val2.
            :rtype: int

        """
        return val1 & val2

    def fonctionXOR(self, val1, val2):
        """
            Fonction qui effectue un XOR bitwise entre deux valeurs.

            Cette fonction permet de retourner le résultat d'un XOR
            logique entre deux valeurs val1 et val2.

            :example:
            >>> fonctionXOR(1, 1)
            0
            >>> fonctionXOR(0, 1)
            1
            >>> fonctionXOR(1, 0)
            1
            >>> fonctionXOR(0, 0)
            0
            >>> fonctionXOR(0xAFAF, 0xFAFA)
            21845

            :param val1: Nombre entier de gauche du XOR logique.
            :type val1: int
            :param val2: Nombre entier de droite du XOR logique.
            :type val2: int

            :return: Résultat du XOR logique entre val1 et val2.
            :rtype: int

        """
        return val1 ^ val2

    def fonctionNOT(self, val):
        """
            Fonction qui effectue un NOT bitwise sur une valeur.

            Cette fonction permet de retourner le résultat d'un NOT
            logique sur une valeur.

            :example:
            >>> fonctionNOT(1)
            0
            >>> fonctionNOT(0)
            1
            >>> fonctionNOT(0xAFAF)
            44976
            >>> fonctionNOT(0xFAFA)
            0xFFFF

            :param val: Nombre entier pour le NOT logique.
            :type val: int

            :return: Résultat du NOT logique de val.
            :rtype: int

        """
        return 0xFFFF - val

    def fonctionLT(self, val1, val2):
        """
            Fonction qui effectue l'évaluation LT entre deux valeurs.

            Cette fonction permet d'évaluation si val1 est plus petit que
            val2 et retourne le résultat (vrai/faux).

            :example:
            >>> fonctionLT(1, 1)
            0
            >>> fonctionLT(0, 1)
            1
            >>> fonctionLT(1, 0)
            0
            >>> fonctionLT(0, 0)
            0
            >>> fonctionLT(0xAFAF, 0xFAFA)
            1

            :param val1: Nombre entier de gauche de l'évaluation LT.
            :type val1: int
            :param val2: Nombre entier de droite de l'évaluation LT.
            :type val2: int

            :return: Résultat de l'évaluation LT entre val1 et val2.
            :rtype: int

        """
        return int(val1 < val2)

    def fonctionGT(self, val1, val2):
        """
            Fonction qui effectue l'évaluation GT entre deux valeurs.

            Cette fonction permet d'évaluation si val1 est plus grand que
            val2 et retourne le résultat (vrai/faux).

            :example:
            >>> fonctionGT(1, 1)
            0
            >>> fonctionGT(0, 1)
            0
            >>> fonctionGT(1, 0)
            1
            >>> fonctionGT(0, 0)
            0
            >>> fonctionGT(0xAFAF, 0xFAFA)
            0

            :param val1: Nombre entier de gauche de l'évaluation GT.
            :type val1: int
            :param val2: Nombre entier de droite de l'évaluation GT.
            :type val2: int

            :return: Résultat de l'évaluation GT entre val1 et val2.
            :rtype: int

        """
        return int(val1 > val2)

    def fonctionLE(self, val1, val2):
        """
            Fonction qui effectue l'évaluation LE entre deux valeurs.

            Cette fonction permet d'évaluation si val1 est plus petit ou
            égal à val2 et retourne le résultat (vrai/faux).

            :example:
            >>> fonctionLE(1, 1)
            1
            >>> fonctionLE(0, 1)
            1
            >>> fonctionLE(1, 0)
            0
            >>> fonctionLE(0, 0)
            1
            >>> fonctionLE(0xAFAF, 0xFAFA)
            1

            :param val1: Nombre entier de gauche de l'évaluation LE.
            :type val1: int
            :param val2: Nombre entier de droite de l'évaluation LE.
            :type val2: int

            :return: Résultat de l'évaluation LE entre val1 et val2.
            :rtype: int

        """
        return int(val1 <= val2)

    def fonctionGE(self, val1, val2):
        """
            Fonction qui effectue l'évaluation LE entre deux valeurs.

            Cette fonction permet d'évaluation si val1 est plus grand ou
            égal à val2 et retourne le résultat (vrai/faux).

            :example:
            >>> fonctionGE(1, 1)
            1
            >>> fonctionGE(0, 1)
            0
            >>> fonctionGE(1, 0)
            1
            >>> fonctionGE(0, 0)
            1
            >>> fonctionGE(0xAFAF, 0xFAFA)
            0

            :param val1: Nombre entier de gauche de l'évaluation GE.
            :type val1: int
            :param val2: Nombre entier de droite de l'évaluation GE.
            :type val2: int

            :return: Résultat de l'évaluation GE entre val1 et val2.
            :rtype: int

        """
        return int(val1 >= val2)

    def fonctionEQ(self, val1, val2):
        """
            Fonction qui effectue l'évaluation EQ entre deux valeurs.

            Cette fonction permet d'évaluation si val1 est égal à val2
            et retourne le résultat (vrai/faux).

            :example:
            >>> fonctionEQ(1, 1)
            1
            >>> fonctionEQ(0, 1)
            0
            >>> fonctionEQ(1, 0)
            0
            >>> fonctionEQ(0, 0)
            1
            >>> fonctionEQ(0xAFAF, 0xFAFA)
            0

            :param val1: Nombre entier de gauche de l'évaluation EQ.
            :type val1: int
            :param val2: Nombre entier de droite de l'évaluation EQ.
            :type val2: int

            :return: Résultat de l'évaluation EQ entre val1 et val2.
            :rtype: int

        """
        return int(val1 == val2)

    def fonctionEZ(self, val):
        """
            Fonction qui vérifie si val est égal à zéro.

            Cette fonction permet d'évaluer si val est égal à zéro.

            :example:
            >>> fonctionEZ(1)
            0
            >>> fonctionEZ(0)
            1
            >>> fonctionEZ(0xAFAF)
            0

            :param val: Nombre entier de l'évaluation EZ.
            :type val: int

            :return: Résultat de l'évaluation EZ entre val.
            :rtype: int

        """
        return int(val == 0x0000)

    def fonctionNZ(self, val):
        """
            Fonction qui vérifie si val n'est pas égal à zéro.

            Cette fonction permet d'évaluer si val n'est égal pas à zéro.

            :example:
            >>> fonctionNZ(1)
            1
            >>> fonctionNZ(0)
            0
            >>> fonctionNZ(0xAFAF)
            1

            :param val: Nombre entier de l'évaluation NZ.
            :type val: int

            :return: Résultat de l'évaluation NZ entre val.
            :rtype: int

        """
        return int(val != 0x0000)


# Activation des doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
