#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 05-Enum.py

    Identification  : 05-Enum
    Titre           : Enum
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 14-04-2017
    Description     : Enum pour les OPCODE's, REGISTRE's, ADRESSAGE's
                      et MODE's.


    Le module ``Enum``
    ================================

    Ce module contient une fonction pour créer des types Enum's. Ce
    module contient aussi des énumérations pour les OPCODE's, les
    REGISTRE's et pour les ADRESSAGE's.


"""


def __enum(**enums):
    """
        Création du type Enum pour le besoin de l'application.

        :return: Un type Enum
        :rtype: Enum

        >>> ENUMTEST = __enum(VRAI = True, FAUX = False)
        >>> ENUMTEST.VRAI
        True
        >>> ENUMTEST.FAUX
        False

    """
    return type('Enum', (), enums)

# Énumération pour le mode du bus.
MODE = __enum(INACTIVE=0x0000, 
              READ=0x0001, 
              WRITE=0x0002,
              RESET=0x0008,
              HALT=0x0009)

# Enumération pour les opérateurs.
OPCODE = __enum(NOP=0x0000,
                JMP=0x0100,
                JMZ=0x0200,
                JMO=0x0300,
                JMC=0x0400,
                SET=0x0500,
                LD=0x0600,
                ST=0x0700,
                MV=0x0800,
                HLT=0x0F00,
                # Commande pour l'ALU.
                ADD=0x1100,
                SUB=0x1200,
                MUL=0x1300,
                DIV=0x1400,
                OR=0x2100,
                AND=0x2200,
                XOR=0x2300,
                NOT=0x2400,
                # Comparateurs.
                LT=0x3100,
                GT=0x3200,
                LE=0x3300,
                GE=0x3400,
                EQ=0x3500,
                EZ=0x3600,
                NZ=0x3700,
                # --Chaine de caractères.
                DTA=0XFFFF)

# Enumération pour le registre.
REGISTRE = __enum(A=0x0001, B=0x0002, C=0x0003, D=0x0004)

# Enumeration pour le type d'adressage.
ADRESSAGE = __enum(IMMEDIATE=0x0000,  # Valeur écrite dans le code
                   DIRECT=0x0010,  # Adresse écrite dans le code
                   INDIRECT=0x0020)  # Adresse dans le registre


# Activation des doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()