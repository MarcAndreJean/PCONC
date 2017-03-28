#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : ProjetConception.py

    Identification  : ProjetConception
    Titre           : Programme principal du projet
    Auteurs         : Francis Emond, Malek Khattech, Marc-André Jean
    Date            : 27-04-2017
    Description     : Démmarrage de l'application.

"""

__author__ = "Francis Emond, Malek Khattech, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

"""
    Le module ``ProjetConception``
    ================================

    Ce module s'occupe tout simplement de démarrer l'application et de
    rassembler tous les modules. Les lignes de code ci-dessous s'occupent
    de démarrer l'interface après que tous les modules soient chargés.

"""

try:
    modVue = __import__("01-Vue")
    modFonctionEditeur = __import__("02-FonctionEditeur")
    modCompileur = __import__("03-Compileur")
    modMicroOrdinateur = __import__("04-Micro-Ordinateur")
except ImportError:
    import importlib
    modVue = importlib.import_module("Modules.01-Vue")
    modFonctionEditeur = importlib.import_module("Modules.02-FonctionEditeur")
    modCompileur = importlib.import_module("Modules.03-Compileur")
    modMicroOrdinateur = importlib.import_module("Modules.04-Micro-Ordinateur")


# Python 2 seulement:
try:
    from Tkinter import *
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *

if __name__ == '__main__':
    # Création de la fenêtre avec une taille initiale.
    root = Tk()
    
    vueGlobal = modVue.VueGlobal(root)  # Création de la vue global.
    vueGlobal.pack(fill=BOTH)
    
    root.wm_minsize(800, 600)
    root.wm_title("Projet Conception - v" + __version__)
    root.configure(background='snow')
    
    # Démarrage de l'application.
    root.mainloop()
