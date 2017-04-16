"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-03-ALU.py

    Identification  : 04-03-ALU
    Titre           : ALU
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 11-04-2017
    Description     : ALU de l'application.


"""
__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Verification"

"""
    Le module ````
    ================================

    Ce module contient l'ALU telle que présentrée dans le
    document de spécification.
"""

class alu:
    """
        class ALU
        ========================

        Cette classe contient la classe ALU. Elle représente l'ALU
        telle que présentée dans le document de
        spécification.


    """
    
    bus =None

    
    def __init__(self,bus):
        """
            Constructeur de la classe ALU

            Le constructeur initialise l'obet de  la classe ALU et le relie au bus
            de donnees
        """
        self.bus = bus
        bus.register(self)
    def Clock(self):
        return
    def event(self):
        return
    def fonctionADD(reg1,reg2):
        """
            FonctionADD
            Cette fonction permet de retourner la somme de reg1 et reg2
        >>>fonctionADD(1,2)
        3
        """
        return reg1+reg2
    def fonctionSUB(reg1,reg2):
        """
            FonctionSUB
            Cette fonction permet de retourner la difference de reg1 et reg2
        >>>fonctionSUB(2,1)
        1
        """
        return reg1-reg2
    def fonctionMUL(reg1,reg2):
        """
            FonctionMUL
            Cette fonction permet de retourner le resultat de la multiplication de reg1 par reg2
        >>>fonctionMUL(2,2)
        4
        """
        return reg1*reg2
    def fonctionDIV(reg1,reg2):
        """
            FonctionDIV
            Cette fonction permet de retourner le resultat de la division entiere de reg1 par reg2
        >>>fonctionDIV(1,3)
        0
        """
        return reg1//reg2
