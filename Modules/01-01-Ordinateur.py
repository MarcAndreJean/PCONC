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
    Date            : 13-04-2017
    Description     : Interface ordinateur de l'application.


    Le module ``VueOrdinateur``
    ================================

    Ce module contient la vue « Ordinateur » telle que présentée dans le
    document de spécification. La classe nommée « VueOrdinateur » gère
    la création des composantes de cette vue. La classe hérite du widget
    Frame pour permettre un placement plus polyvalent et une réutilisation
    plus aisée de cette vue.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation des modules nécessaires.
try:
    modFunctEditor = __import__("02-FonctionEditeur")
    modComputer = __import__("04-Micro-Ordinateur")
    modCompiler = __import__("03-Compileur")
except ImportError:
    import importlib
    modFunctEditor = importlib.import_module("Modules.02-FonctionEditeur")
    modComputer = importlib.import_module("Modules.04-Micro-Ordinateur")
    modCompiler = importlib.import_module("Modules.03-Compileur")

# Importation de Tkinter selon la version de Python.
# Python 2 seulement:
try:
    from Tkinter import *
    import ttk as ttk
    import tkFileDialog as fileDialog
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *
    import tkinter.ttk as ttk
    import tkinter.filedialog as fileDialog


def __enum(**enums):
    """
        Création du type Enum pour le besoin de l'application.

        :return: Un type Enum
        :rtype: Enum

    """
    return type('Enum', (), enums)


# Enum des différents types d'utilisation de la Vue Ordinateur
# NORMAL = Utilisation avec l'application.
# LIGNECOMMANDE = Utilisation en ligne de commande.
TypeUse = __enum(NORMAL=1, LIGNECOMMANDE=2)


class VueOrdinateur(Frame):
    """
        class VueOrdinateur
        ========================

        Cette classe hérite d'un Frame. Elle représente la vue
        « Ordinateur » telle que présentée dans le document de
        spécification.

        >>> test = VueOrdinateur()

    """

    # Constructeur.
    def __init__(self, parent=None, typeUse=TypeUse.NORMAL):
        """
            Constructeur de la classe VueOrdinateur.

            Le constructeur initialise le Frame de la classe avec le Widget
            parent donné en argument. Il initialise ensuite les Widgets
            nécessaires de la vue (comme décrit dans le document de
            spécification). La vue crée un objet "Micro-Ordinateur" à partir
            du module "04-Micro-Ordinateur". Cet objet sera lié (bind)
            aux évènements associés (par exemple les boutons de la vue).

            Il y a deux types de façon de créer cette vue, le mode
            NORMAL (par défaut) et le mode LIGNECOMMANDE. Le mode
            normal inclut des boutons pour charger un programme
            exécutable, pour le réinitialiser et pour générer des
            coups d'horloge. Le mode « ligne de commande » inclut
            une zone de texte et une entrée pour interprétée en
            temps réel du code assembleur.

            :example:
            >>> test1 = VueOrdinateur(Tk(), TypeUse.NORMAL)
            >>> test2 = VueOrdinateur(Tk(), TypeUse.LIGNECOMMANDE)

            :param parent: Parent Widget de la classe.
            :type parent: Widget (Tk)

            .. warning:: Cette classe a besoin d'avoir accès au module
                         « 04-Micro-Ordinateur ».


        """
        # Crée un Micro-Ordinateur pour cette interface
        self.computer = modComputer.MicroOrdinateur()
        self.boolClock = False

        # Initialise le Frame de l'instance.
        Frame.__init__(self, parent)

        # Création des widgets nécessaires.
        # --StringVar.
        self.txtvarToggleClock = StringVar()
        self.txtvarToggleClock.set("Démarrer l'horloge")
        self.txtvarConsoleOutput = StringVar()
        self.txtvarConsoleOutput.set("Console Output")
        self.txtvarCMDhisto = StringVar()

        # En mode NORMAL on crée des boutons pour charger un exécutable,
        # et des boutons pour l'exécuter (Réinitialiser, Générer coup
        # d'horloge et Démarrer/Arrêter horloge).
        if typeUse == TypeUse.NORMAL:
            # --Button.
            self.frameBut = Frame(self)
            self.butCharger = ttk.Button(
                self.frameBut, text="Charger programme")
            self.butReset = ttk.Button(self.frameBut, text="Réinitialiser")
            self.butTick = ttk.Button(self.frameBut,
                                      text="Générer un coup d'horloge")
            self.butClock = ttk.Button(self.frameBut,
                                       textvariable=self.txtvarToggleClock)
            self.butCharger.pack(fill=X, padx=3, pady=10, ipady=20)
            self.butReset.pack(fill=X, padx=30, pady=3, ipady=10)
            self.butTick.pack(fill=X, padx=10, pady=3, ipady=12)
            self.butClock.pack(fill=X, padx=10, pady=3, ipady=12)
            self.frameBut.grid(column=0, row=1, sticky="WE")
        # En mode LIGNECOMMANDE on crée une entrée (ENTRY) pour la saisie
        # de code en ligne de commande, et au dessus de cette entrée on
        # y mets une zone de texte pour afficher l'historique du code.
        else:
            # --Button.
            self.frameCMD = Frame(self)
            self.labelCMD = ttk.Label(self.frameCMD,
                                      text="Ligne de commande")
            self.txtCMDhisto = ttk.Label(
                self.frameCMD,
                textvariable=self.txtvarCMDhisto,
                width=0,
                relief=GROOVE,
                background="white",
                anchor=SW)
            self.entryCMD = ttk.Entry(self.frameCMD)
            self.labelCMD.pack(fill=X, padx=3, pady=5)
            self.txtCMDhisto.pack(fill=BOTH, padx=3, pady=5, expand=True)
            self.entryCMD.pack(fill=X, padx=3, pady=10)
            self.frameCMD.grid(column=0, row=0, rowspan=3, sticky="NSWE")
        # End

        # --Label.
        self.frameCout = Frame(self)
        self.labelCout = ttk.Label(self.frameCout,
                                   text="Console Output")
        self.txtConsoleOutput = ttk.Label(
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
        self.labelCin = ttk.Label(self.frameCin,
                                  text="Console Input")

        self.innerFrameCin = ttk.Frame(self.frameCin, relief=SUNKEN)
        self.txtConsoleInput = Text(self.innerFrameCin, width=0, relief=FLAT)
        self.labelCin.pack(fill=X, padx=3, pady=5)
        self.innerFrameCin.pack(fill=BOTH,
                                padx=3, pady=5, expand=True)
        self.txtConsoleInput.pack(fill=BOTH, padx=3, pady=3, expand=True)
        self.frameCin.grid(column=2, row=0, rowspan=3, sticky="NSWE")
        # --Notebook.
        self.tabMemoireChooser = ttk.Notebook(self, width=0)
        self.tabMemoireChooser.grid(column=3, row=0, rowspan=3,
                                    sticky="NSWE",
                                    padx=3, pady=8)
        # --Listbox.
        self.listMemoireRAM = Listbox(self.tabMemoireChooser,
                                      state=DISABLED, relief=FLAT)
        self.listMemoireROM = Listbox(self.tabMemoireChooser,
                                      state=DISABLED, relief=FLAT)
        self.listMemoireIO = Listbox(self.tabMemoireChooser,
                                     state=DISABLED, relief=FLAT)

        # Insertion des listes dans le TAB mémoire.
        self.tabMemoireChooser.add(self.listMemoireRAM, text="    RAM    ")
        self.tabMemoireChooser.add(self.listMemoireROM, text="    ROM    ")
        self.tabMemoireChooser.add(self.listMemoireIO, text="      IO      ")

        # Création du Grid inclut dans le parent.
        # Fixation d'un "poids" pour chacune des cellules, pour que les
        # cellules s'étire et que le «Grid» remplit l'espace requis.
        for y in range(3):
            self.grid_rowconfigure(y, minsize=100, weight=1)
        if typeUse == TypeUse.NORMAL:
            for x in range(1, 4):
                self.grid_columnconfigure(x, minsize=200, weight=2)
            self.grid_columnconfigure(0, minsize=100, weight=1)
        else:
            for x in range(4):
                self.grid_columnconfigure(x, minsize=200, weight=2)

        # Liaison des évènements.
        if typeUse == TypeUse.NORMAL:
            self.butCharger.configure(command=self.__callbackCharger)
            self.butReset.configure(command=self.__callbackReset)
            self.butTick.configure(command=self.__callbackTick)
            self.butClock.configure(command=self.__callbackClock)
        else:
            self.entryCMD.bind('<Return>', self.__callbackCMD)

        # Fin de __init__.
        return

    def __callbackCMD(self, event):
        """
            Callback pour la ligne de commande.

            Cette fonction est appelée lorsque l'utilisateur confirme
            l'entrée avec la touche retour du clavier. Elle essaie de
            compiler la ligne de code. Si la compilation est un succès,
            nous l'exécutons dans le micro-ordinateur. Autrement, nous
            faisons «flasher» le code illégal.

            :param event: Évènement clavier.
            :type event: Event

            ..note: Cette fonction est interne à la classe.

        """
        # Compilation du code en bytecode.
        result = modCompiler.compile(self.entryCMD.get())
        # Si la compilation est un succès on l'exécute.
        if result[0]:
            self.entryCMD.delete(0, END)
            self.computer.execute(result[1])
        # Sinon on avertit l'utilisateur de l'erreur.
        else:
            fg = self.entryCMD.cget("foreground")
            fgnot = "red"
            self.entryCMD.configure(foreground=fgnot)
            self.after(100, lambda: self.entryCMD.configure(foreground=fg))
            self.after(200, lambda: self.entryCMD.configure(foreground=fgnot))
            self.after(300, lambda: self.entryCMD.configure(foreground=fg))
        return

    def __callbackCharger(self):
        """
            Callback pour le bouton «Charger».

            Cette fonction appelle la fonction appropriée du module
            02-FonctionEditeur. On ouvre une boite système pour faire
            choisir l'emplacement du fichier code à charger. Nous appelons
            ensuite la fonction pour charger ce fichier.

            ..note: Cette fonction est interne à la classe.

        """
        # On demande le chemin du fichier à charger.
        info = fileDialog.askopenfilename(
            defaultextension=".exeb",
            filetypes=[("Executable byte code", ".exeb")],
            title="Charger l'exécutable...")
        # --Si l'utilisateur annule.
        if info is "":
            return
        # On charge ce fichier.
        code = modFunctEditor.loadCode(info)
        # On appelle la fonction approprié pour charger le code dans
        # le micro-ordinateur.
        self.computer.load(code)
        # Fin de callbackCharger.
        return

    def __callbackReset(self):
        """
            Réinitialise le micro-ordinateur avec le précédent exécutable.

            Cette fonction appelle la fonction appropriée dans le module
            04-Micro-Ordinateur pour réinitialiser l'état de la machine
            virtuelle.

            ..note: Cette fonction est interne à la classe.

        """
        # On appelle la fonction approprié.
        self.computer.reset()
        # Fin de callbackReset.
        return

    def __callbackTick(self):
        """
            Donne un coup d'horloge au micro-ordinateur.

            Cette fonction appelle la fonction appropriée dans le module
            04-Micro-Ordinateur pour donner un coup d'horloge à la machine
            virtuelle.

            ..note: Cette fonction est interne à la classe.

        """
        # On appelle la fonction approprié.
        self.computer.tick()
        # Fin de callbackTick.
        return

    def __callbackClock(self):
        """
            Active/Désactive l'horloge du micro-ordinateur.

            Cette fonction appelle la fonction appropriée dans le module
            04-Micro-Ordinateur pour activer/désactiver l'horloge de la
            machine virtuelle.

            ..note: Cette fonction est interne à la classe.

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

            :example:
            >>> test = VueOrdinateur(None)
            >>> isinstance(test.getListRAM(), Listbox)
            True

        """
        return self.listMemoireRAM

    def getListROM(self):
        """
            Retourne le widget liste de la ROM.

            :return: Retourne le widget liste de la ROM.
            :rtype: Listbox

            :example:
            >>> test = VueOrdinateur(None)
            >>> isinstance(test.getListROM(), Listbox)
            True

        """
        return self.listMemoireROM

    def getListIO(self):
        """
            Retourne le widget liste des IO.

            :return: Retourne le widget liste des IO.
            :rtype: Listbox

            :example:
            >>> test = VueOrdinateur(None)
            >>> isinstance(test.getListIO(), Listbox)
            True

        """
        return self.listMemoireIO

    def appendConsoleOutput(self, output):
        """
            Ajoute à la fin du « log » une nouvelle sortie.

            Cette fonction ajoute une nouvelle ligne de texte (à la fin)
            pour l'historique de la console de sortie du micro-ordinateur.

            :param output: Texte à ajouter à la fin de la console.
            :type output: str

            :example:
            >>> test = VueOrdinateur(None)
            >>> test.appendConsoleOutput("test")


        """
        self.txtvarConsoleOutput.set(self.txtvarConsoleOutput.get() + '\n' + output)
        # Fin de appendConsoleOutput.
        return


# Activation des doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
