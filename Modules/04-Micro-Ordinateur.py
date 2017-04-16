#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-Micro-Ordinateur.py

    Identification  : 04-Micro-Ordinateur
    Titre           : Micro-Ordinateur
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 15-04-2017
    Description     : Micro-Ordinateur. Rassemble les composantes et
                      initialise l'émulation.


    Le module ``Micro-Ordinateur``
    ================================

    Ce module contient une classe nommée « Micro-Ordinateur » qui gère les
    composantes (Bus, CPU, Clock et Mémoire). C'est le chef-d'orchestre
    pour l'émulation et c'est lui qui est responsable du bon fonctionnement
    du micro-ordinateur. La Clock est compris dans le micro-ordinateur comme
    dans l'horloge à l'intérieur de la carte-mère d'un ordinateur.


"""

__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "production"

# Importation des modules nécessaires.
try:
    modBus = __import__("04-01-Bus")
    modCPU = __import__("04-02-CPU")
    modMemoire = __import__("04-04-Memoire")
except ImportError:
    import importlib
    modBus = importlib.import_module("Modules.04-01-Bus")
    modCPU = importlib.import_module("Modules.04-02-CPU")
    modMemoire = importlib.import_module("Modules.04-04-Memoire")

from threading import Thread


class MicroOrdinateur():
    """
        class MicroOrdinateur
        ========================

        Cette classe s'occupe de l'émulation du MicroOrdinateur.

        :example:
        >>> test = MicroOrdinateur()

        ..note: L'horloge est intégré au micro-ordinateur. La fonction
                tick() et toggleClock() fait appel à fonction clock()
                du Bus dans un Thread pour permettre une utilisation
                asynchrone du micro-ordinateur et de la GUI.

    """

    def __init__(self, extracomponents=[]):
        """
            Contrusteur de la classe Micro-Ordinateur.

            Cette fonction crée les composantes de bases du
            micro-ordinateur. Elle attache des composantes
            supplémentaires (pour permettre une compatibilité pour
            une réutilisation ou utilisation externe de cette classe).

            :param extracomponents: Liste de composants supplémentaires.
            :type extracomponents: List

            ..note: Les composants devraient être une classe ayant une
                    méthode nommée event() et une méthode nommée clock().

        """
        # État de la Clock.
        self.clockActive = False
        self.clockThread = None
        # Création du bus.
        self.bus = modBus.Bus()
        # On register le micro-ordinateur pour l'horloge.
        self.bus.register(self)
        # Création des composants de base du Micro-Ordinateur.
        self.cpu = modCPU.CPU(self.bus)
        self.memoire = modMemoire.CPU(self.bus)
        # Attachement des composants supplémentaires (s'il y a lieu).
        self.xtracomp = extracomponents
        if extracomponent is not None and len(extracomponents) > 0:
            for xcomp in extracomponents:
                self.bus.register(xcomp)
        # Fin de __init__.
        return

    def load(self, bytecode):
        """
            Fonction pour charger bytecode dans la ROM un programme.

            Cette fonction charge un programme (celui dans bytecode) dans
            la mémoire ROM du micro-ordinateur.

            :example:
            >>> test = MicroOrdinateur()
            >>> test.load([0xFAFA, 0xAFAF, 0x0000, 0xFFFF])

            :param bytecode: Tableau de int (16 bits) d'un programme
                             exécutable.
            :type bytecode: int[]

        """
        # On réinitialise le micro-ordinateur.
        self.reset()
        self.memoire.uploadProgram(bytecode)
        return

    def reset(self):
        """
            Fonction pour réinitialiser le micro-ordinateur.

            Cette fonction réinitialise la mémoire (sauf la ROM), les
            états et informations du CPU, et les informations sur le
            bus.

            :example:
            >>> test = MicroOrdinateur()
            >>> test.reset()
            >>> test.memoire.getMemory(0xFFFF) == 0x0000
            True

        """
        # On s'assure que le clock n'est pas en marche.
        self.clockActive = False
        if clockThread is not None and clockThread.isAlive():
            clockThread.join()
        # On réinitialise les composants de base.
        self.bus.reset()
        # Fin de la fonction.
        return

    def tick(self):
        """
            Fonction pour produire un coup d'horloge.

            Cette fonction produit un coup d'horloge dans le bus
            duquel il propagera ce coup aux travers des autres
            composantes.

            :example:
            >>> test = MicroOrdinateur()
            >>> test.tick()

        """
        # Nous créons un Thread anonyme puisqu'il mourra après l'appel
        # de bus.clock().
        if not clockActive:
            # Si le thread n'a pas terminé on attends au moins
            # sa terminaison.
            if clockThread is not None and clockThread.isAlive():
                clockThread.join()
            # On crée le thread.
            self.clockThread = Thread(target=self.bus.clock)
            self.clockThread.start()
        return

    def toggleClock(self):
        """
            Fonction pour changer l'état de l'horloge.

            Cette fonction active/désactiver l'horloge dépendant
            de son état actuel.

            :example:
            >>> test = MicroOrdinateur()
            >>> test.tick()
            
        """
        # Nous changons la valeur d'état du clock.
        self.clockActive = not self.clockActive
        # Si l'état est maintenant actif pour la clock, nous recréons
        # thread pour celui-ci.
        if clockActive:
            # Si le thread n'a pas terminé on attends au moins
            # sa terminaison.
            if clockThread is not None and clockThread.isAlive():
                clockThread.join()
            # On crée le thread.
            self.clockThread = Thread(target=self.bus.clock)
            self.clockThread.start()
        return

    def event():
        """
            Event pour le clock.

            Event pour le clock. Si un OPCODE a terminé ces «computations»
            et que le bus est maintenant en arrêt (en attente d'un nouveau
            coup d'horloge), et bien nous lui donnons un nouveau coup
            d'horloge.

           ..note: La fonction ne donne aucun coup d'horloge si clockActive
                   est devenu inactif.

        """
        # On donne un coup d'horloge si l'horloge est active.
        if clockActive:
            self.bus.clock()
        return


# Activation des doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
