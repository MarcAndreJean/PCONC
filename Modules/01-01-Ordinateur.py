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
    modCin = __import__("01-05-TextCin")
    modFunctEditor = __import__("02-FonctionEditeur")
    modComputer = __import__("04-Micro-Ordinateur")
    modCompiler = __import__("03-Compileur")
    modListener = __import__("06-ListenerGUI")
except ImportError:
    import importlib
    modCin = importlib.import_module("Modules.01-05-TextCin")
    modFunctEditor = importlib.import_module("Modules.02-FonctionEditeur")
    modComputer = importlib.import_module("Modules.04-Micro-Ordinateur")
    modCompiler = importlib.import_module("Modules.03-Compileur")
    modListener = importlib.import_module("Modules.06-ListenerGUI")

# Importation de Tkinter selon la version de Python.
# Python 2 seulement:
try:
    from Tkinter import *
    import ttk as ttk
    import tkFileDialog as fileDialog
    import tkFont
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *
    import tkinter.ttk as ttk
    import tkinter.filedialog as fileDialog
    import tkFont


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

intTOascii = {0x0030: '0', 0x0031: '1', 0x0032: '2', 0x0033: '3',
              0x0034: '4', 0x0035: '5', 0x0036: '6', 0x0037: '7',
              0x0038: '8', 0x0039: '9',
              0x0041: 'A', 0x0042: 'B', 0x0043: 'C', 0x0044: 'D',
              0x0045: 'E', 0x0046: 'F', 0x0047: 'G', 0x0048: 'H',
              0x0049: 'I', 0x004A: 'J', 0x004B: 'K', 0x004C: 'L',
              0x004D: 'M', 0x004E: 'N', 0x004F: 'O', 0x0050: 'P',
              0x0051: 'Q', 0x0052: 'R', 0x0053: 'S', 0x0054: 'T',
              0x0055: 'U', 0x0056: 'V', 0x0057: 'W', 0x0058: 'X',
              0x0059: 'Y', 0x005A: 'Z',
              0x0061: 'a', 0x0062: 'b', 0x0063: 'c', 0x0064: 'd',
              0x0065: 'e', 0x0066: 'f', 0x0067: 'g', 0x0068: 'h',
              0x0069: 'i', 0x006A: 'j', 0x006B: 'k', 0x006C: 'l',
              0x006D: 'm', 0x006E: 'n', 0x006F: 'o', 0x0070: 'p',
              0x0071: 'q', 0x0072: 'r', 0x0073: 's', 0x0074: 't',
              0x0075: 'u', 0x0076: 'v', 0x0077: 'w', 0x0078: 'x',
              0x0079: 'y', 0x007A: 'z',
              0x000A: ' ', 0x0020: ' '}


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
        self.computer = modComputer.MicroOrdinateur(
            [modListener.ListenerGUI(self)])
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
        self.frameCinCout = Frame(self)
        self.labelCout = ttk.Label(self.frameCinCout,
                                   text="Console Output",
                                   anchor=SW)
        self.txtConsoleOutput = ttk.Label(
            self.frameCinCout,
            font=tkFont.Font(family='Consolas', size=8),
            textvariable=self.txtvarConsoleOutput,
            width=0,
            relief=GROOVE,
            background="white",
            anchor=NW)
        self.labelCout.pack(fill=X, padx=3, pady=5)
        self.txtConsoleOutput.pack(fill=X, padx=3, pady=5)
        self.frameCinCout.grid(column=1, row=0, rowspan=3, sticky="NSWE")
        # ----Initialise label.text
        self.stringOuput = ''
        sentence = '........................................' \
                   '........................................'
        for y in range(24):
            self.stringOuput += sentence + '\n'
        self.stringOuput += sentence
        self.txtvarConsoleOutput.set(self.stringOuput)

        # --Text.
        self.labelCin = ttk.Label(self.frameCinCout,
                                  text="Console Input")

        self.innerFrameCin = ttk.Frame(self.frameCinCout)
        self.scllbrCin = ttk.Scrollbar(self.innerFrameCin)
        self.txtConsoleInput = modCin.TextCin(
            self.innerFrameCin,
            width=0,
            bd=2,
            height=0,
            yscrollcommand=self.scllbrCin.set)
        self.scllbrCin.config(command=self.txtConsoleInput.yview)
        self.labelCin.pack(fill=X, padx=3, pady=5)
        self.innerFrameCin.pack(fill=BOTH,
                                padx=3, pady=5, expand=True)
        self.txtConsoleInput.pack(side=LEFT, fill=BOTH, padx=3, pady=3,
                                  expand=True)
        self.scllbrCin.pack(side=RIGHT, fill=Y)
        # --Notebook.
        self.tabMemoireChooser = ttk.Notebook(self, width=0)
        self.tabMemoireChooser.grid(column=2, row=0, rowspan=3,
                                    sticky="NSWE",
                                    padx=3, pady=8)
        # --Listbox.
        # ----Frame pour Listbox.
        self.frameMemrom = Frame(self.tabMemoireChooser)
        self.frameMemram = Frame(self.tabMemoireChooser)
        self.frameMemio = Frame(self.tabMemoireChooser)
        self.frameMemreg = Frame(self.tabMemoireChooser)
        # ----Scrollbar pour Listbox.
        self.scllbrMemrom = ttk.Scrollbar(self.frameMemrom)
        self.scllbrMemram = ttk.Scrollbar(self.frameMemram)
        self.scllbrMemio = ttk.Scrollbar(self.frameMemio)
        self.scllbrMemreg = ttk.Scrollbar(self.frameMemreg)
        # ----ListBox.
        self.listMemoireROM = ttk.Treeview(
            self.frameMemrom, show="headings", columns=(
                "one", "two", "three"), yscrollcommand=self.scllbrMemrom.set)
        self.listMemoireRAM = ttk.Treeview(
            self.frameMemram, show="headings", columns=(
                "one", "two", "three"), yscrollcommand=self.scllbrMemram.set)
        self.listMemoireIO = ttk.Treeview(self.frameMemio,
                                          show="headings",
                                          columns=("one", "two", "three"),
                                          yscrollcommand=self.scllbrMemio.set)
        self.listMemoireREG = ttk.Treeview(
            self.frameMemreg, show="headings", columns=(
                "one", "two", "three"), yscrollcommand=self.scllbrMemreg.set)
        # Création des colonnes.
        for listMemoire in [self.listMemoireROM, self.listMemoireRAM,
                            self.listMemoireIO, self.listMemoireREG]:
            listMemoire.column("one", width=50)
            listMemoire.column("two", width=50)
            listMemoire.column("three", width=50)
            listMemoire.heading("one", text="Adresse")
            listMemoire.heading("two", text="Valeur (hex)")
            listMemoire.heading("three", text="Valeur (dec)")
        # Insertion des éléments.
        # --ROM.
        for i in range(0, 0x40FB + 1):
            self.listMemoireROM.insert("", 'end', iid=str(i),
                                       values=('0x' + format(i, '#06X')[2:],
                                               "0x0000", "0"))
        # --RAM.
        for i in range(0x8000, 0xFFFF + 1):
            self.listMemoireRAM.insert("", 'end', iid=str(i),
                                       values=('0x' + format(i, '#06X')[2:],
                                               "0x0000", "0"))
        # --IO.
        for i in range(0x40FC, 0x7FFF + 1):
            self.listMemoireIO.insert("", 'end', iid=str(i),
                                      values=('0x' + format(i, '#06X')[2:],
                                              "0x0000", "0"))
        # --REG.
        self.listMemoireREG.insert("", 'end', iid="RegA",
                                   values=("RegA",
                                           "0x0000", "0"))
        self.listMemoireREG.insert("", 'end', iid="RegB",
                                   values=("RegB",
                                           "0x0000", "0"))
        self.listMemoireREG.insert("", 'end', iid="RegC",
                                   values=("RegC",
                                           "0x0000", "0"))
        self.listMemoireREG.insert("", 'end', iid="RegD",
                                   values=("RegD",
                                           "0x0000", "0"))
        self.listMemoireREG.insert("", 'end', iid="RegP",
                                   values=("RegP",
                                           "0x0000", "0"))
        self.listMemoireREG.insert("", 'end', iid="RegI",
                                   values=("RegI",
                                           "0x0000", "0"))
        self.listMemoireREG.insert("", 'end', iid="RegS",
                                   values=("RegS",
                                           "0x0000", "0"))
        # Liaison scrollbar et tree.
        self.scllbrMemrom.config(command=self.listMemoireROM.yview)
        self.scllbrMemram.config(command=self.listMemoireRAM.yview)
        self.scllbrMemio.config(command=self.listMemoireIO.yview)
        self.scllbrMemreg.config(command=self.listMemoireREG.yview)
        # Placement du scrollbar et tree dans le frame.
        # --rom.
        self.scllbrMemrom.pack(side="right", fill="y")
        self.listMemoireROM.pack(side="left", fill=BOTH, expand=True)
        # --ram.
        self.scllbrMemram.pack(side="right", fill="y")
        self.listMemoireRAM.pack(side="left", fill=BOTH, expand=True)
        # --io.
        self.scllbrMemio.pack(side="right", fill="y")
        self.listMemoireIO.pack(side="left", fill=BOTH, expand=True)
        # --reg.
        self.scllbrMemreg.pack(side="right", fill="y")
        self.listMemoireREG.pack(side="left", fill=BOTH, expand=True)
        # --Frame.
        self.frameMemrom.pack(fill=BOTH, expand=True)
        self.frameMemio.pack(fill=BOTH, expand=True)
        self.frameMemram.pack(fill=BOTH, expand=True)
        self.frameMemreg.pack(fill=BOTH, expand=True)

        # Insertion des listes dans le TAB mémoire.
        self.tabMemoireChooser.add(self.frameMemrom, text="    ROM    ")
        self.tabMemoireChooser.add(self.frameMemio,
                                   text="      IO      ")
        self.tabMemoireChooser.add(self.frameMemram, text="    RAM    ")
        self.tabMemoireChooser.add(self.frameMemreg, text="    REG    ")

        # Création du Grid inclut dans le parent.
        # Fixation d'un "poids" pour chacune des cellules, pour que les
        # cellules s'étire et que le «Grid» remplit l'espace requis.
        for y in range(3):
            self.grid_rowconfigure(y, minsize=100, weight=1)
        if typeUse == TypeUse.NORMAL:
            for x in range(1, 3):
                self.grid_columnconfigure(x, minsize=200, weight=2)
            self.grid_columnconfigure(0, minsize=100, weight=1)
        else:
            for x in range(3):
                self.grid_columnconfigure(x, minsize=200, weight=2)

        # Liaison des évènements.
        if typeUse == TypeUse.NORMAL:
            self.butCharger.configure(command=self.__callbackCharger)
            self.butReset.configure(command=self.__callbackReset)
            self.butTick.configure(command=self.__callbackTick)
            self.butClock.configure(command=self.__callbackClock)
        else:
            self.entryCMD.bind('<Return>', self.__callbackCMD)
        self.bind("<Key>", self.__callbackKey)

        # Fin de __init__.
        return

    def __callbackKey(self, event):
        """
        """
        print(event.char)
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
            self.txtvarCMDhisto.set(
                self.txtvarCMDhisto.get() + self.entryCMD.get() + '\n')
            temptext = str(self.txtvarCMDhisto.get()).splitlines()
            # Suppression des lignes excédentaires.
            if len(temptext) > 33:
                self.txtvarCMDhisto.set(
                    str(self.txtvarCMDhisto.get())[len(temptext[0]) + 1:])
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
        code = modFunctEditor.loadByteCode(info)

        # On réinitialise l'affichage.
        # --ROM.
        for i in range(0, 0x40FB + 1):
            self.listMemoireROM.item(str(i),
                                     values=('0x' + format(i, '#06X')[2:],
                                             "0x0000", "0"))
        self.__callbackReset()

        # On mets à jour la liste de ROM.
        # On parcourt toutes les adresses de la mémoire ROM.
        for address in range(min(len(code), 0x40FB + 1)):
            # On transfert le bytecode[address] à l'adresse.
            self.listMemoireROM.item(str(address),
                                     values=('0x' + format(address, '#06X')[2:],
                                             format(code[address], '#06x'),
                                             str(code[address])))

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
        # ----Reinitialise label.text
        self.stringOuput = ''
        sentence = '........................................' \
                   '........................................'
        for y in range(24):
            self.stringOuput += sentence + '\n'
        self.stringOuput += sentence
        self.txtvarConsoleOutput.set(self.stringOuput)

        # ----Reinitialise les listes.
        # --RAM.
        for i in range(0x8000, 0xFFFF + 1):
            self.listMemoireRAM.item(str(i),
                                     values=('0x' + format(i, '#06X')[2:],
                                             "0x0000", "0"))
        # --IO.
        for i in range(0x40FC, 0x7FFF + 1):
            self.listMemoireIO.item(str(i),
                                    values=('0x' + format(i, '#06X')[2:],
                                            "0x0000", "0"))
        # --REGISTRE.
        for curreg in ("RegA", "RegB", "RegC", "RegD", "RegP", "RegI", "RegS"):
            self.listMemoireREG.item(curreg, values=(curreg, "0x0000", "0"))

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
        if self.boolClock:
            self.txtvarToggleClock.set("Arrêter l'horloge")
        else:
            self.txtvarToggleClock.set("Démarrer l'horloge")
        # Fin de callbackClock.
        return

    def updateMemory(self, address, value):
        """
            Mets à jour la GUI pour l'adresse «address».

            Cette fonction est appelé lorsqu'il y a un changement dans la
            mémoire du micro-ordinateur. Dépendamment de la valeur de
            l'adresse en argument (address), la fonction fera les
            changements en conséquent.

            :example:
            >>> test = VueOrdinateur(None)
            >>> test.updateMemory(0, 14)

            :param address: Adresse qui a été mise à jour.
            :param address: int (16 bits)
            :param value: Valeur à cette adresse.
            :param value: int (16 bits)

        """
        # Registre
        if isinstance(address, str):
            self.listMemoireREG.item(str(address),
                                     values=(address,
                                             format(value, '#06x'),
                                             str(value)))
            self.listMemoireREG.update_idletasks()
            self.listMemoireREG.update()
        # Espace ROM
        elif address <= 0x40FB:
            self.listMemoireROM.item(
                str(address),
                values=(
                    '0x' +
                    format(
                        address,
                        '#06X')[
                        2:],
                    format(
                        value,
                        '#06x'),
                    str(value)))
            self.listMemoireROM.update_idletasks()
            self.listMemoireROM.update()
        # Espace IO
        elif address <= 0x7FFF:
            self.listMemoireIO.item(str(address),
                                    values=('0x' + format(address, '#06X')[2:],
                                            format(value, '#06x'),
                                            str(value)))
            # Screen : Ouput
            if address >= 0x41FC and address <= 0x49CB:
                global intTOascii
                self.stringOuput = self.stringOuput[:address - 0x41FC] + \
                    str(intTOascii.get(value, '.')) + \
                    self.stringOuput[1 + address - 0x41FC:]
                self.txtvarConsoleOutput.set(self.stringOuput)
            # Keyboard
            elif address >= 0x40FC and address <= 0x41FB:
                pass
            self.listMemoireIO.update_idletasks()
            self.listMemoireIO.update()
        # Espace RAM
        elif address <= 0xFFFF:
            self.listMemoireRAM.item(
                str(address),
                values=(
                    '0x' +
                    format(
                        address,
                        '#06X')[
                        2:],
                    format(
                        value,
                        '#06x'),
                    str(value)))
            self.listMemoireRAM.update_idletasks()
            self.listMemoireRAM.update()

        # Fin.
        return


# Activation des doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
