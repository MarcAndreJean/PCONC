#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-02-Editeur.py

    Identification  : 01-02-Editeur
    Titre           : Interface Editeur
    Auteurs         : Francis Emond, Malek Khattech, Marc-André Jean
    Date            : 27-04-2017
    Description     : Interface editeur de l'application.


"""

__author__ = "Francis Emond, Malek Khattech, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"


#try:
#    __import__("01-01-Ordinateur")
#    __import__("01-02-Editeur")
#except ImportError:
#    import importlib
#    importlib.import_module("Modules.01-01-Ordinateur")
#    importlib.import_module("Modules.01-02-Editeur")


# Python 2 seulement:
try:
    from Tkinter import *
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *

"""
    Le module ``VueEditeur``
    ================================

    Description

"""

class VueEditeur(Frame):
    """
        class VueEditeur
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

