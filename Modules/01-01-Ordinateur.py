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
    Date            : 10-04-2017
    Description     : Interface ordinateur de l'application.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation des modules nécessaires.
try:
    modComputer = __import__("04-Micro-Ordinateur")
except ImportError:
    import importlib
    modComputer = importlib.import_module("Modules.04-Micro-Ordinateur")

# Importation de Tkinter selon la version de Python.
# Python 2 seulement:
try:
    from Tkinter import *
    from ttk import *
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
        # Crée un Micro-Ordinateur pour cette interface
        self.computer = modComputer.MicroOrdinateur()
        self.code = ""
        self.boolClock = False

        # Initialise le Frame de l'instance.
        Frame.__init__(self, parent)

        # Création des widgets nécessaires.
        # --StringVar.
        self.txtvarToggleClock = StringVar()
        self.txtvarToggleClock.set("Démarrer l'horloge")
        self.txtvarConsoleOutput = StringVar()
        self.txtvarConsoleOutput.set("Console Output")
        # --Button.
        self.frameBut = Frame(self)
        self.butCharger = Button(self.frameBut, text="Charger programme")
        self.butReset = Button(self.frameBut, text="Réinitialiser")
        self.butTick = Button(self.frameBut,
                              text="Générer un coup d'horloge")
        self.butClock = Button(self.frameBut,
                               textvariable=self.txtvarToggleClock)
        self.butCharger.pack(fill=X, padx=3, pady=10, ipady=20)
        self.butReset.pack(fill=X, padx=30, pady=3, ipady=10)
        self.butTick.pack(fill=X, padx=10, pady=3, ipady=12)
        self.butClock.pack(fill=X, padx=10, pady=3, ipady=12)
        self.frameBut.grid(column=0, row=1, sticky="WE")
        # --Label.
        self.frameCout = Frame(self)
        self.labelCout = Label(self.frameCout,
                               text="Console Output")
        self.txtConsoleOutput = Label(
            self.frameCout,
            textvariable=self.txtvarConsoleOutput,
            width=0,
            relief=GROOVE,
            background="white",
            anchor=SW)
        self.labelCout.pack(fill=X, padx=3, pady=5)
        self.txtConsoleOutput.pack(fill=BOTH, padx=3, pady=5, expand=True)
        self.frameCout.grid(column=1, row=0, rowspan=3, sticky="NSWE")
        # --Text.
        self.frameCin = Frame(self)
        self.labelCin = Label(self.frameCin, anchor=S,
                              text="Console Input")

        self.innerFrameCin = Frame(self.frameCin, relief=SUNKEN)
        self.txtConsoleInput = Text(self.innerFrameCin, width=0, relief=FLAT)
        self.labelCin.pack(fill=X, padx=3, pady=5)
        self.innerFrameCin.pack(fill=BOTH,
                                padx=3, pady=5, expand=True)
        self.txtConsoleInput.pack(fill=BOTH, padx=3, pady=3, expand=True)
        self.frameCin.grid(column=2, row=0, rowspan=3, sticky="NSWE")
        # --Notebook.
        self.tabMemoireChooser = Notebook(self, width=0)
        self.tabMemoireChooser.grid(column=3, row=0, rowspan=3,
                                    sticky="NSWE",
                                    padx=3, pady=8)
        # --Listbox.
        self.listMemoireRAM = Listbox(self.tabMemoireChooser)
        self.listMemoireROM = Listbox(self.tabMemoireChooser)
        self.listMemoireIO = Listbox(self.tabMemoireChooser)

        # Insertion des listes dans le TAB mémoire.
        self.tabMemoireChooser.add(self.listMemoireRAM, text="RAM")
        self.tabMemoireChooser.add(self.listMemoireROM, text="ROM")
        self.tabMemoireChooser.add(self.listMemoireIO, text="IO")

        # Création du Grid inclut dans le parent.
        # Fixation d'un "poids" pour chacune des cellules, pour que les
        # cellules s'étire et que le «Grid» remplit l'espace requis.
        for y in range(3):
            self.grid_rowconfigure(y, weight=1)
        for x in range(1, 4):
            self.grid_columnconfigure(x, weight=1)
        self.grid_columnconfigure(0, weight=0)

        # Liaison des évènements.
        self.butCharger.configure(command=self.callbackCharger)
        self.butReset.configure(command=self.callbackReset)
        self.butTick.configure(command=self.callbackTick)
        self.butClock.configure(command=self.callbackClock)

        # Fin de __init__.
        return

    def callbackCharger(self):
        # Fin de callbackCharger.
        return

    def callbackReset(self):
        """
            Réinitialise le micro-ordinateur avec le précédent exécutable.

            Cette fonction appelle la fonction appropriée dans le module
            04-Micro-Ordinateur pour réinitialiser l'état de la machine
            virtuelle (et en rechargeant en mémoire le dernier exécutable
            charger ultérieurement, s'il y a eu lieu).


        """
        # On appelle la fonction approprié.
        self.computer.reset(self.code)
        # Fin de callbackReset.
        return

    def callbackTick(self):
        """
            Donne un coup d'horloge au micro-ordinateur.

            Cette fonction appelle la fonction appropriée dans le module
            04-Micro-Ordinateur pour donner un coup d'horloge à la machine
            virtuelle.


        """
        # On appelle la fonction approprié.
        self.computer.tick()
        # Fin de callbackTick.
        return

    def callbackClock(self):
        """
            Active/Désactive l'horloge du micro-ordinateur.

            Cette fonction appelle la fonction appropriée dans le module
            04-Micro-Ordinateur pour activer/désactiver l'horloge de la
            machine virtuelle.


        """
        # On appelle la fonction approprié.
        self.computer.toggleClock()
        self.boolClock = not self.boolClock
        if (self.boolClock):
            self.txtvarToggleClock.set("Arrêter l'horloge")
        else:
            self.txtvarToggleClock.set("Démarrer l'horloge")
        # Fin de callbackClock.
        return

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
        # Fin de appendConsoleOutput.
        return self
