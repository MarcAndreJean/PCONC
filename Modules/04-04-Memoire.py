#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-04-Memoire.py

    Identification  : 04-04-Memoire
    Titre           : Module memoire
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 11-04-2017
    Description     : Module mémoire de l'ordinateur.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Production"

# Importation des modules nécessaires.


"""
    Le module ``Mémoire``
    ================================

    Ce module le composant mémoire de l'ordinateur, tel que	
    présenté dans le document de spécification.

"""


class Memoire:
    """
        class Memoire
        ========================

        Cette classe représente le composant  « Memoire » tel que
        présenté dans le document de spécification. 

    """

    # Constructeur.
    def __init__(self, The_Bus, romTab, ioTab, ramTab):
        """
            Constructeur de la classe Memoire

        """
        # --Bus.
	self.bus = The_Bus #Objet bus déjà créé ppar l'ordinateur et passé en paramètre
	The_Bus.register(self)

        # --Memory mapping.
	self.rom = romTab	#adr values 0-16635
	self.io = ioTab		#adr values 16636-32767
	self.ram = ramTab 	#adr values 32768-65535

    def event(self):
        """
            Fonction event.
	    


        """
	
       return

    def clock(self):
	"""
	    Fonction clock.


	"""

    	return
	
    def setMemory(self, adr, value):
	"""
	    Fonction setMemory.
	    Cette fonction permet de modifier la valeur d'une case mémoire (adr) pour celle donnée en argument (value).
	
	    :param adr: Adresse de la case mémoire a modifier
	    :type adr: Int
	    :param value: Nouvelle valeur a inscrire dans la mémoire
	    :type value: Int

	    :Example:
	    
	    >>>setMemory(self, 32768, 12345)
	    >>>setMemory(self, 1000, -123)
	    >>>self.ram[32768]
	    12345
	    >>>self.ram[1000]
	    -123
	    >>>self.ram[0]
	    0
	 
	"""

    	self.ram[adr] = value

    def getMemory(self, adr):
	"""
	    Fonction getMemory.
	    Cette fonction permet d'aller chercher la valeur d'une case mémoire donnée (adr).

	    :param adr: Adresse de la case mémoire dont la valeur est retournée	
	    :type adr: Int
	    :return: Retourne la valeur de la case mémoire 'adr'.
	    :rtype: Int

	    :Example:
	    >>>setMemory(self, 32768, -400)
	    >>>setMemory(self, 2222, 999)
	    >>>getMemory(self, 0)
	    0
	    >>>getMemory(self, 32768)
	    -400
	    >>>getMemory(self, 2222)
	    999

	"""

    	return self.ram[adr]
