#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 01-04-CodeScrolledText.py

    Identification  : 01-04-CodeScrolledText
    Titre           : Widget : Texte avec défilement et numéro de ligne
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 10-04-2017
    Description     : Un widget Tk qui représente une ScrolledText avancé.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation de Tkinter selon la version de Python.
# Python 2 seulement:
try:
    from Tkinter import *
    import ttk as ttk
# Python 2 et 3 (Python 2 après ''pip install future''):
except ImportError:
    from tkinter import *
    import tkinter.ttk as ttk

"""
    Le module ``CodeScrolledText``
    ================================

    Ce module contient une classe nommée « CodeScrolledText » qui est
    un widget similaire à «ScrolledText» mais plus avancé pour la
    programmation. Il s'agit d'un Widget qui n'existe pas dans la
    bibliothèque de Tkinter (Python). Cette classe utilise deux classes
    « TextwLineNumbers » et « TextAvanced ». TextwLineNumbers est un
    Canvas Tk qui est utilisé ici pour « redessiner » les numéros de ligne.
    TextAvanced est tout simplement un Widget Text à lequel on ajoute un
    évènement qui est déclencher lors de l'ajout ou la suppression de
    ligne. CodeScrolledText, quand à elle, s'occupe de lié ces deux classes
    avec une ScrollBar.


"""


class TextwLineNumbers(Canvas):
    """
        Classe qui hérite de Canvas. Cette classe est utilisé pour
        redessiner les numéros de ligne accompagné avec le
        « textwidget ».


    """

    def __init__(self, *args, **kwargs):
        """
            Constructeur de TextwLineNumbers.

            Le constructeurs prend en argument *args et **kwargs pour
            une construction plus complexe du canvas si désiré.

        """
        Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None
        return

    def attach(self, argtextwidget):
        """
            Fonction qui attache le Widget Text « argtextwidget ».

            Cette fonction attache le Widget Text « argtextwidget »
            à la classe. Celui-ci devrait être de type « TextAdvanced »
            pour que cette classe puisse redessiner les lignes.

            :param argtextwidget: Widget Text du Canvas.
            :type argtextwidget: TextAdvanced


        """
        self.textWidget = argtextwidget
        return

    def redraw(self, *args):
        """
            Redessine les numéros de lignes dans le canvas.

            Lorsque cette classe est attaché au TextAdvanced et que
            celui-ci déclenche sont event, cette fonction est
            appelé et les numéros de lignes sont redessinées.
        """
        # Nous supprimons tous du canvas.
        self.delete("all")
        # On remets l'index au début.
        i = self.textWidget.index("@0,0")
        # Pour toutes les lignes existantes nous redéfinisons:
        while True:
            dline = self.textWidget.dlineinfo(i)
            # On quitte la boucle lorsque nous avons parcouru la boucle
            if dline is None:
                break
            y = dline[1]
            # On quitte si nous avons dépasser le nombre maximal en ROM
            if y > 16635:
                break
            # On érit le format en Hex (4 bytes) et on l'imprime
            linetext = format(int(str(i).split(".")[0])-1, '#06x')
            self.create_text(2, y, anchor="nw", text=linetext)
            i = self.textWidget.index("%s+1line" % i)


class TextAdvanced(Text):
    """
        TextAvanced est tout simplement un Widget Text à lequel on ajoute
        un évènement qui est déclencher lors de l'ajout ou la suppression
        de ligne.


    """

    def __init__(self, *args, **kwargs):
        """
            Constructeur de TextAdvanced.

            Le constructeurs prend en argument *args et **kwargs pour
            une construction plus complexe du Text si désiré.


        """
        # Initialisation de Text avec les arguments.
        Text.__init__(self, *args, **kwargs)

        # Création des évènements pour l'insertion ou la supression de
        # ligne dans la zone de texte, ou lorsque le texte est
        # « scrolled ».
        self.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # On fait un appel avec le vrai tk Widget avec ces args.
                set result [uplevel [linsert $args 0 $widget_command]]

                # On génère les évènements pour les différents types
                # de commandes.
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) ||
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Change>> -when tail
                }

                # On retourne le résultat.
                return $result
            }
            ''')
        self.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(self)))
        return


class CodeScrolledText(Frame):
    """
        class CodeScrolledText
        ========================

        Cette classe hérite d'un Widget Frame. Elle y inclut un Widget
        Text, un Widget Label et un Widget Scrollbar.


    """

    def __init__(self, parent):
        """
            Constructeur de CodeScrolledText.

            Le constructeur initialise son Frame avec le parent qui est
            donné en argument. Il initialise ses composantes.

            :param parent: Widget Parent de la classe.
            :type parent: Widget (Tk)


        """
        # Initialistion du status bar.
        Frame.__init__(self, parent)

        # --Initialisation de la scrollbar.
        self.scrollbar = Scrollbar(self)

        # --Initialisation de la zone de code.
        self.editArea = TextAdvanced(self, yscrollcommand=self.scrollbar.set)
        # --Initialisation de la zone de numéro de ligne.
        self.linenumbers = TextwLineNumbers(self, width=40)
        self.linenumbers.attach(self.editArea)

        # Configuration du tout.
        self.scrollbar.config(command=self.editArea.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y", expand=True)
        self.editArea.pack(side="left", fill="both", expand=True)

        # Liaison des fonctions ultérieurement écrites (voir plus haut
        # dans TextAdvanced) avec TextwLineNumbers.
        self.editArea.bind("<<Change>>", self._on_change)
        self.editArea.bind("<Configure>", self._on_change)

        # Fin de __init__.
        return

    def _on_change(self, event):
        """
            Event pour la mise à jour des lignes.

            Cette fonction est appelé par le TextAdvanced lors d'une
            modification pour permettre la mise à jour du canvas et
            des numéros de lignes avec TextwLineNumbers.redraw().

            :param event: Informations de l'évènement.
            :type event: Tk Event

        """
        self.linenumbers.redraw()
        return

    def get(self, start, stop):
        """
            Wrapper pour la fonction get du TextAdvanced.

            Cette fonction est un wrapper pour la fonction get()
            du TextAdvanced.

            :param start: Position début du texte à extraire.
            :type start: str
            :param stop: Position fin du texte à extraire.
            :type stop: Indexes

            :return: Retourne le texte désiré.
            :rtype: str

        """
        return self.editArea.get(start, stop)
