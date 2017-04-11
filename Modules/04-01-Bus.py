"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-01-Bus.py

    Identification  : 04-01-Bus
    Titre           : Bus de donnees
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 10-04-2017
    Description     : Bus de donnees de l'application.


"""
__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Verification"

"""
    Le module ````
    ================================

    Ce module contient le Bus telle que présentrée dans le
    document de spécification.


"""
class Bus:
      """
        class Bus
        ========================

        Cette classe contient la classe bus. Elle représente le Bus
        telle que présentée dans le document de
        spécification.


    """
    component =[] #liste des composantes de la machine
    data=0        # valeur sur le bus
    adress=0      # adreese d'operation
    mode=0        # 0:inerte 1:write 2:read
    a = 1         # condition d'arret de la boucle while de la fonction clock
    def __init__(self):
        """
            Constructeur de la classe Bus.

            Le constructeur initialise l'obet de  la classe bus. En plus
            de la fonction event et clock elle contient la fonction
            register qui permet d'ajouter des composanta a la liste «component »
          
        """
        # Initialisation du composant
        return

    def register(self,component):
        """
            Fonction register.
            Cette fonction permet d'ajouter des elements dans la liste des composantes de l'ordinateur
            elle possede comme parametre le composant a ajouter dans la liste «component ».
        """

        self.component.append(component)
        return

    def event(self):
        """
            Fonction event.
            Cette fonction verifie la valeur se trouvant sur le bus et permet a l'odinateur d'adopter le comportement adequat. Elle
            appelle les fonctions event de event des composantes se trouvant dans la liste «component »
        """
        
        if self.component:
            for i in self.component:
                if i.event():
                    i.event()
        
        return

    def Clock(self):
        """
            Fonction Clock.
            Cette fonction controle le traitement et l'executon des instructions en agissant particulierement sur le cpu. Elle
            appelle les fonctions clock des composantes se trouvant dans la liste «component »
            
        """
        while(self.a):
            if self.component:
                for i in self.component:
                    if i.Clock():
                        i.Clock()
            self.a=0
            
        
        return
# fin de la classe

