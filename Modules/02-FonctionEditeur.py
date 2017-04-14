#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 02-FonctionEditeur.py

    Identification  : 02-FonctionEditeur.py
    Titre           : Interface Ordinateur
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 13-04-2017
    Description     : Interface ordinateur de l'application.


    Le module ``FonctionEditeur``
    ================================

    Ce module contient ...


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"


def saveCode(path, code):
    """
        Titre

        Descriptions

        :example:
        >>> saveCode("C:\Windows\test.asm", "mov 10 acc")

        :param path:
        :type path: str
        :param code:
        :type code: str

        
    """
    fichier = open(path,"w")
    fichier.write(code)
    fichier.close()



def loadCode(path):
    """
        Titre

        Descriptions

        :example:
        >>> saveCode("C:\Windows\test.asm")
        "mov 10 acc"

        :param path:
        :type path: str
        :return:
        :rtype: str

        

    """
    fichier = open(path,"r")
    code = fichier.read()
    fichier.close()
    return code
