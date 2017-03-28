#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-Vue.py

    Identification  : 01-Vue
    Titre           : GUI principal
    Auteurs         : Francis Emond, Malek Khattech, Marc-André Jean
    Date            : 27-04-2017
    Description     : GUI principal de l'application.


"""

__author__ = "Francis Emond, Malek Khattech, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"


try:
    modOrdinateur = __import__("01-01-Ordinateur")
    modEditeur = __import__("01-02-Editeur")
except ImportError:
    import importlib
    modOrdinateur = importlib.import_module("Modules.01-01-Ordinateur")
    modEditeur = importlib.import_module("Modules.01-02-Editeur")


# Python 2 seulement:
try:
    from Tkinter import *
    from Tkinter.ttk import *
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *
    from tkinter.ttk import *

"""
    Le module ``Vue``
    ================================

    Ce module s'occupe de l'affichage de la vue global de l'application
    avec la librairie Tkinter de Python. Elle contient une classe VueGlobal
    qui s'occupe des deux sous-vues (Ordinateur et Editeur).

"""

class VueGlobal(Frame):
    """
        class VueGlobal
        ========================

        Description


    """

    # Constructeur.
    def __init__(self, parent = None):
        """
            Title

            Description

            :param parent:
            :type parent:

            .. warning::
        """
        # Initialise le Frame de l'instance.
        Frame.__init__(self, parent)
        # Crée la composante graphique qui va controler le gui Ordinateur
        # et Editeur avec un tabs.
        self.vueTabs = Notebook(self)
        self.vueOrdinateur = modOrdinateur.VueOrdinateur(self.vueTabs)
        self.vueEditeur = modEditeur.VueEditeur(self.vueTabs)
        self.vueTabs.pack(fill=BOTH, padx=2, pady=3)
        self.vueOrdinateur.pack(fill=BOTH)
        self.vueEditeur.pack(fill=BOTH)
        self.vueTabs.add(self.vueOrdinateur, text="Ordinateur")
        self.vueTabs.add(self.vueEditeur, text="Editeur")

