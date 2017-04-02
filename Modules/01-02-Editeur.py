#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-02-Editeur.py

    Identification  : 01-02-Editeur
    Titre           : Interface Editeur
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 27-04-2017
    Description     : Interface editeur de l'application.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation des modules nécessaires.
try:
    modFunctEditor = __import__("02-FonctionEditeur")
    modCompiler = __import__("03-Compileur")
except ImportError:
    import importlib
    modFunctEditor = importlib.import_module("Modules.02-FonctionEditeur")
    modCompiler = importlib.import_module("Modules.03-Compileur")
    

# Importation de Tkinter selon la version de Python.
# Python 2 seulement:
try:
    from Tkinter import *
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *

"""
    Le module ``VueEditeur``
    ================================

    Ce module contient la vue « Editeur » telle que présentrée dans le
    document de spécification.


"""


class VueEditeur(Frame):
    """
        class VueEditeur
        ========================

        Cette classe hérite d'un Frame. Elle représente la vue
        « Editeur » telle que présentée dans le document de
        spécification. Le Frame inclut les boutons et autres Widgets
        nécessaires pour la vue.


    """

    # Constructeur.
    def __init__(self, parent=None):
        """
            Constructeur de la classe VueOrdinateur.

            Le constructeur initialise le Frame de la classe avec le Widget
            parent donné en argument. Il initialise ensuite les Widgets
            nécessaires de la vue (comme décrit dans le document de
            spécification). Les fonctions du module « 02-FonctionEditeur »
            et du module « 03-Compileur » seront liés aux évènements
            associés (par exemple les boutons de la vue).

            :param parent: Parent Widget de la classe.
            :type parent: Widget (Tk)

            .. warning:: Cette classe a besoin d'avoir accès aux modules
                         « 02-FonctionEditeur » et « 03-Compileur ».


        """
        # Initialise le Frame de l'instance.
        Frame.__init__(self, parent)

        # TODO: Écrire du code x')
