#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-01-Ordinateur.py

    Identification  : 01-01-Ordinateur
    Titre           : Interface Ordinateur
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 27-04-2017
    Description     : Interface ordinateur de l'application.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation des modules nécessaires.
modComputer = __import__("04-Micro-Ordinateur")

# Importation de Tkinter selon la version de Python.
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

    Ce module contient la vue « Ordinateur » telle que présentrée dans le
    document de spécification.


"""


class VueOrdinateur(Frame):
    """
        class VueOrdinateur
        ========================

        Cette classe hérite d'un Frame. Elle représente la vue
        « Ordinateur » telle que présentée dans le document de
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
            spécification). La vue crée un objet "Micro-Ordinateur" à partir
            du module "04-Micro-Ordinateur". Cet objet sera lié (linked)
            aux évènements associés (par exemple les boutons de la vue).

            :param parent: Parent Widget de la classe.
            :type parent: Widget (Tk)

            .. warning:: Cette classe a besoin d'avoir accès au module
                         « 04-Micro-Ordinateur ».


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
        # --StringVar.
        self.txtvarToggleClock = StringVar()
        self.txtvarToggleClock.set("Démarrer l'horloge")
        self.txtvarConsoleOutput = StringVar()
        self.txtvarConsoleOutput.set("Console Output")
        # --Button.
        self.butCharger = Button(self, text="Charger programme")
        self.butReset = Button(self, text="Réinitialiser")
        self.butTick = Button(self, text="Générer un coup d'horloge")
        self.butClock = Button(self, textvariable=self.txtvarToggleClock)
        # --Label.
        self.txtConsoleOutput = Label(self,
                                      textvariable=self.txtvarConsoleOutput)
        # --Text.
        self.txtConsoleInput = Text(self)
        # --Notebook.
        self.tabMemoireChooser = Notebook(self)
        # --Listbox.
        self.listMemoireRAM = Listbox(self.tabMemoireChooser)
        self.listMemoireROM = Listbox(self.tabMemoireChooser)
        self.listMemoireIO = Listbox(self.tabMemoireChooser)

        # Insertion des listes dans le TAB mémoire.
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
        # TODO: Régler la vue (grid, pack, etc.)
        # TODO: Création et linkage du Micro-Ordinateur.

    def setTextButToggleClock(self, text):
        """
            Accesseur (setter) pour le texte du bouton « Démarrer/Arrêter
            l'horloge »

            Cette fonction renomme le bouton « Démarrer/Arrêter l'horloge ».

            :param text: Nouveau texte du bouton.
            :type text: str


        """
        self.txtvarToggleClock.set(text)

    def getListRAM(self):
        """
            Retourne le widget liste de la RAM.

            :return: Retourne le widget liste de la RAM.
            :rtype: Listbox


        """
        return self.listMemoireRAM

    def getListROM(self):
        """
            Retourne le widget liste de la ROM.

            :return: Retourne le widget liste de la ROM.
            :rtype: Listbox


        """
        return self.listMemoireROM

    def getListIO(self):
        """
            Retourne le widget liste des IO.

            :return: Retourne le widget liste des IO.
            :rtype: Listbox


        """
        return self.listMemoireIO

    def appendConsoleOutput(self, output):
        """
            Ajoute à la fin du « log » une nouvelle sortie.

            Cette fonction ajoute une nouvelle ligne de texte (à la fin)
            pour l'historique de la console de sortie du micro-ordinateur.

            :param output: Texte à ajouter à la fin de la console.
            :type output: str


        """
        self.txtvarConsoleOutput += output
