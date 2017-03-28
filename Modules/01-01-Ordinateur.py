#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-01-Ordinateur.py

    Identification  : 01-01-Ordinateur
    Titre           : Interface Ordinateur
    Auteurs         : Francis Emond, Malek Khattech, Marc-André Jean
    Date            : 27-04-2017
    Description     : Interface ordinateur de l'application.


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
    from Tkinter.ttk import *
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *
    from tkinter.ttk import *

"""
    Le module ``VueOrdinateur``
    ================================

    Description

"""

class VueOrdinateur(Frame):
    """
        class VueOrdinateur
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
        
        # Création du Grid inclut dans le parent.
        # Fixation d'un "poids" pour chacune des cellules, pour que les
        # cellules s'étire et que le «Grid» remplit l'espace requis.
        for x in range(7):
            Grid.rowconfigure(self, x, weight=1)
        for y in range(4):
            Grid.columnconfigure(self, y, weight=1)
        
        # Création des widgets nécessaires.
        self.txtvarToggleClock = StringVar()
        self.txtvarToggleClock.set("Démarrer l'horloge")
        self.txtvarConsoleOutput = StringVar()
        self.txtvarConsoleOutput.set("Console Output")

        self.butCharger = Button(self, text="Charger programme")
        self.butReset = Button(self, text="Réinitialiser")
        self.butTick = Button(self, text="Générer un coup d'horloge")
        self.butClock = Button(self, textvariable=self.txtvarToggleClock)

        self.txtConsoleOutput = Label(self,
                                      textvariable=self.txtvarConsoleOutput)

        self.txtConsoleInput = Text(self)

        self.tabMemoireChooser = Notebook(self)

        self.listMemoireRAM = Listbox(self.tabMemoireChooser)
        self.listMemoireROM = Listbox(self.tabMemoireChooser)
        self.listMemoireIO = Listbox(self.tabMemoireChooser)

        # Insertion des listes dans le TAB mémoire
        self.tabMemoireChooser.add(self.listMemoireRAM, text="RAM")
        self.tabMemoireChooser.add(self.listMemoireROM, text="ROM")
        self.tabMemoireChooser.add(self.listMemoireIO, text="IO")
        
        # Placement dans le Grid.
        self.butCharger.grid(sticky=(N, S, W, E), column=0, row=2)
        self.butReset.grid(sticky=(N, S, W, E), column=0, row=3)
        self.butTick.grid(sticky=(N, S, W, E), column=0, row=4)
        self.butClock.grid(sticky=(N, S, W, E), column=0, row=5)
        
        self.txtConsoleOutput.grid(sticky=(N, S, W, E),
                                   column=1, row=0, rowspan=7)
        self.txtConsoleInput.grid(sticky=(N, S, W, E),
                                   column=2, row=0, rowspan=7)
        self.tabMemoireChooser.grid(sticky=(N, S, W, E),
                                   column=3, row=0, rowspan=7)
    
    
    def setTextButToggleClock(self, text):
        """
            Title

            Description

            :param parent:
            :type parent:
        """
        self.txtvarToggleClock.set(text)


    def getListPlageMemoire(self):
        """
            Title

            Description

            :param parent:
            :type parent:
        """
        pass


    def appendConsoleOutput(self, output):
        """
            Title

            Description

            :param parent:
            :type parent:
        """
        self.txtvarConsoleOutput += output
