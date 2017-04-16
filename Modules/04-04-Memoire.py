#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-04-Memoire.py

    Identification  : 04-04-Memoire
    Titre           : Mémoire
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 15-04-2017
    Description     : Module mémoire du Micro-Ordinateur.


    Le module ``Mémoire``
    ================================

    Ce module est le composant mémoire de l'ordinateur, tel que	
    présenté dans le document de spécification.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"


# Importation des modules nécessaires.
try:
    modEnum = __import__("05-Enum")
    __import__("04-01-Bus")
except ImportError:
    import importlib
    modEnum = importlib.import_module("Modules.05-Enum")
    importlib.import_module("Modules.04-01-Bus")
# Redéfinition.
MODE = modEnum.MODE


class Memoire:
    """
        class Memoire
        ========================

        Cette classe représente le composant « Memoire » tel que
        présenté dans le document de spécification. 
        

    """

    # Constructeur.
    def __init__(self, bus):
        """
            Constructeur de la classe Memoire.

			Le constructeur s'occupe d'initialiser la mémoire et lie
			ce composant avec le bus.

			:param bus: Composant Bus du Micro-Ordinateur.
			:type bus: Bus

        """
        # Bus.
        self.bus = bus
        bus.register(self)

		# Tableau de int pour représenter la mémoire.
        self._data = [0]*(0xFFFF + 1)
        return
    
    def event(self):
        """
            Récepteur pour le signal event.

            Cette fonction est appelé lorsqu'un event est émit
            sur le bus. Elle gère l'écriture et la lecture en mémoire.
            
        """
        # Si en mode LECTURE:
        if (self.bus.mode == MODE.READ):
            # On mets la valeur de la case mémoire à l'adresse bus.address
            # dans le bus.data.
            self.bus.data = self._data[self.bus.address]
            self.bus.mode = MODE.INACTIVE
        # Si en mode ÉCRITURE:
        elif (bus.mode == MODE.WRITE):
            # On mets la valeur de bus.data dans la case mémoire
            # à l'adresse bus.address.
            self._data[self.bus.address] = self.bus.data
            self.bus.mode = MODE.INACTIVE
        return

    def clock(self):
        """
            Récepteur pour le signal clock.

            Cette fonction est appelé lorsqu'un coup d'horloge est émit
            sur le bus. Elle gère la réinitialisation de la mémoire si
            le bus est en mode RESET.
            
        """
        # On réinitialise la mémoire si le bus est en mode reset.
        if (bus.mode == MODE.RESET):
            for i in range (0x40FB + 1, 0xFFFF + 1):
                self._data[i] = 0x0000
        # Fin de la fonction.
        return
    
    def uploadProgram(self, bytecode):
        """
            Fonction pour charger bytecode dans la ROM.

            Cette fonction charge un programme (celui dans bytecode) dans
            la mémoire ROM.

            :example:
            >>> test = Memoire()
            >>> test.uploadProgram([0xFAFA, 0xAFAF, 0x0000, 0xFFFF])

            :param bytecode: Tableau de int (16 bits) d'un programme
                             exécutable.
            :type bytecode: int[]
            
            
        """
        # On parcourt toutes les adresses de la mémoire ROM.
        for adresse in range(min(len(bytecode), 0x40FB + 1)):
            # On transfert le bytecode[adresse] à l'adresse.
            self._data[adresse] = bytecode[adresse]
        # Si le bytecode est plus petit que la taille max de la mémoire
        # ROM, on mets dans zéro pour le reste des cases.
        if len(bytecode) < 0x40FB + 1:
            # On attribut des zéros pour ces cases.
            for adresse in range(len(bytecode), 0x40FB + 1):
            self._data[adresse] = 0x0000
        # Fin.
        return

# Activation des doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()