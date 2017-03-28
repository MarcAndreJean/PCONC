#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-03-StatusBar.py

    Identification  : 01-03-StatusBar
    Titre           : Barre de status
    Auteurs         : Francis Emond, Malek Khattech, Marc-André Jean
    Date            : 27-04-2017
    Description     : Un widget Tk qui représente une barre de status.


"""

__author__ = "Francis Emond, Malek Khattech, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"


# Python 2 seulement:
try:
    from Tkinter import *
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *

"""
    Le module ``StatusBar``
    ================================

    Description

"""

class StatusBar(Frame):
    """
    """
    def __init__(self, parent):
        """
        """
        Frame.__init__(self, parent)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)
        
    def set(self, format, *args):
        """
        """
        self.label.config(text=format % args)
        self.label.update_idletasks()
        
    def clear(self):
        """
        """
        self.label.config(text="") 
        self.label.update_idletasks()
