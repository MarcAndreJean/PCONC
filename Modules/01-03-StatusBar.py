#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-03-StatusBar.py

    Identification  : 01-03-StatusBar
    Titre           : Widget : Barre de status
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 10-04-2017
    Description     : Un widget Tk qui représente une barre de statut.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation de Tkinter selon la version de Python.
# Python 2 seulement:
try:
    from Tkinter import *
    import ttk as ttk
    import tkFont
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *
    import tkinter.ttk as ttk
    import tkFont

"""
    Le module ``StatusBar``
    ================================

    Ce module contient une classe nommée « StatusBar » qui est une barre de
    statut comme dans les programmes populaires courants. Il s'agit d'un
    Widget qui n'existe pas dans la bibliothèque de Tkinter (Python).


"""


class StatusBar(Frame):
    """
        class StatusBar
        ========================

        Cette classe hérite d'un Widget Frame. Elle y inclut un Widget
        Label pour contenir le texte de notre StatusBar. La classe a deux
        fonctions (excluant le constructeur) pour aiser l'affichage du
        texte.


    """

    def __init__(self, parent):
        """
            Constructeur de StatusBar.

            Le constructeur initialise son Frame avec le parent qui est
            donné en argument. Il initialise un Label et l'ajoute dans le
            Frame.

            :param parent: Widget Parent de la classe.
            :type parent: Widget (Tk)


        """
        # Initialistion du status bar.
        Frame.__init__(self, parent)
        self.label = Label(
            self,
            borderwidth=1,
            relief=GROOVE,
            anchor=W,
            background="#bfbfbf",
            font=tkFont.Font(
                size=12))
        self.label.pack(fill=BOTH, expand=TRUE)
        # Fin de __init__.
        return

    def setText(self, format, *args):
        """
            Accesseur (setter) du texte de la StatusBar.

            Cette fonction établit un nouveau texte pour la StatusBar.
            Il est possible d'envoyer des arguments dans la fonction pour
            une personnalisation du texte plus avancée (se référer à
            Label.config() dans la documentation de Tkinter).

            :param format: Nouveau texte de la StatusBar.
            :type format: str

            :param args: Arguments de configuration.
            :type args: str


        """
        # Modification du text.
        self.label.config(text=format % args)
        self.label.update_idletasks()
        # Fin de setText.
        return self

    def clear(self):
        """
            Effacement du texte de la StatusBar.

            Cette fonction efface le texte de la StatusBar. Cela résultera
            en une StatusBar vide.


        """
        # Effacement du text.
        self.label.config(text="")
        self.label.update_idletasks()
        # Fin de clear.
        return
