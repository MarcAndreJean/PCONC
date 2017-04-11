"""
    Projet          : Editeur, Compilateur et Micro-Ordinateur pour
                      un langage assembleur.
    Nom du fichier  : 04-02-CPU.py

    Identification  : 04-02-CPU
    Titre           : Bus de donnees
    Auteurs         : Francis Emond, Malek Khattech,
                      Mamadou Dia, Marc-André Jean
    Date            : 28-04-2017
    Description     : CPU de l'application.


"""
__author__ = "Francis Emond, Malek Khattech, Mamadou Dia, Marc-Andre Jean"
__version__ = "1.0"
__status__ = "Verification"

"""
    Le module ````
    ================================

    Ce module contient le CPU telle que présentré dans le
    document de spécification.


"""
class cpu:
    """
        class CPU
        ========================

        Cette classe contient la classe cpu. Elle représente le CPU
        telle que présentée dans le document de
        spécification.
    """
    bus = None
    pc=0           # program counter - contient l'adresse de la prochaine instruction
    code= []       # instruction to execute
    alu =0         # ALU
    lines =[]      # instructions du rom
    a=0            # instruction
    b=0            # valeur 1
    c=0            # code de l'operation 2
    d =0           # registre à utiliser
    regA=0         # registre A
    regB=0         # registre B
    regC=0         # registre C
    regD=0         # registre D
    Status=[16]    # registre de Status
    memory={}      # memoire
    

    registres ={'1':regA,'2':regB,'3':regC,'4':regD} #registre de A-D;
    registres['5']=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # ajout du registre de Status
 
    
    
    def __init__(self,bus):
        """
            Constructeur de la classe CPU.

            Le constructeur initialise l'obet de  la classe CPU. En plus
            de la fonction event et clock elle contient la fonction register qui permet de lier le CPU à
            un Bus
          
        """
        #Connexion avec le bus
        self.bus = bus
        bus.register(self)
    def event(self):
        """
            Fonction event.
            Cette fonction verifie la valeur se trouvant sur le bus et permet a l'odinateur d'adopter le comportement adequat.
        """
        #print("cpu event")
        return 
    def Fetch(self):
        """
            Fonction Fetch.
            Cette fonction permet d'aller chercher l'instruction se trouvant à l'adresse contenue dans self.pc. Elle fait intervenir le bus en mode Read et
            depose l'instruction dans self.code en la faisant transiter par self.bus.data. Elle incrémente ensuite self.pc
            
        """
        self.bus.mode = 2=
        self.bus.data = lines[self.pc].split()
        self.code = self.bus.data
        self.bus.mode = 0
        self.pc = self.pc+1
      
    def Decode(self):
        """
            Fonction Fetch.
            Cette fonction permet d'aller chercher l'instruction se trouvant à l'adresse contenue dans self.pc. Elle fait intervenir le bus en mode Read et
            depose l'instruction dans self.code en la faisant transiter par self.bus.data. Elle incrémente ensuite self.pc
            
        """
    
          
        if len(self.code)==2:
            self.a=int(self.code[0])  # a ccnserve l'instruction
            self.b=self.code[1]  # b contient la valaur a modifier
            self.c=(self.a & 65280) # code de l'operation
            self.d = (self.a & 15) # registre à considerer dans le cas d'un stranfert
            
        if self.c in [4352,4608,4864,5120,8448,8704,8960]:
            print("operation de l'alu ne rien faire")
          
        if self.c not in [4352,4608,4864,5120,8448,8704,8960]:
            if self.c in [1536,1792]:
                
                # il va y avoir accès mémoire
                self.bus.mode = 2
                print("le bus est en mode write")
                self.bus.adress = self.b
                self.bus.data = self.registres[str(self.d)]
                print("le bus contient la valeur a modifier et l'adresse ou faire la moficication")
            if self.c not in [1536,1792]:
                # pas d'acces memoire
                print("operation simple au niveau du cpu donc on peut passer à l'execution")
                      
      
          
                
                
    def Execute(self):
        """
            Fonction Fetch.
            Cette fonction permet d'aller chercher l'instruction se trouvant à l'adresse contenue dans self.pc. Elle fait intervenir le bus en mode Read et
            depose l'instruction dans self.code en la faisant transiter par self.bus.data. Elle incrémente ensuite self.pc
            
        """
        if self.c==1280:
            self.registres[str(self.d)] = int(self.code[1])
        if self.c==1792 or self.c==1536:
            self.memory[self.b] = int(self.bus.data)
        if self.c ==2048:
            self.registres[str(self.d)] = self.memory[self.b]
        if self.c==9216:
            print("la fonction NOT est à completer")
        if self.c==12544:
            if self.registres[str(self.d)]< self.registres[self.b]:
                self.registres['5'][12]=1
                print("self.registres['5'][12]= ",self.registres['5'][12])
            else:
                print("dans le else ")
                self.registres['5'][12]=0
        if self.c==12800:
            if self.registres[str(self.d)]> self.registres[self.b]:
                self.registres['5'][12]=1
                      
            else:
                print("dans le else ")
                self.registres['5'][12]=0
          
        if self.c==13056:
            if self.registres[str(self.d)]<= self.registres[self.b]:
                self.registres['5'][12]=1
                      
            else:
                print("dans le else ")
                self.registres['5'][12]=0
          
        if self.c==13312:
            if self.registres[str(self.d)]>= self.registres[self.b]:
                self.registres['5'][12]=1
            else:
                print("dans le else ")
                self.registres['5'][12]=0

        if self.c==13568:
            if self.registres[str(self.d)]== self.registres[self.b]:
                self.registres['5'][12]=1
                      
            else:
                print("dans le else ")
                self.registres['5'][12]=0
        if self.c == 256:
            self.pc = int(self.b)
        if self.c == 512:
            if self.registre['5'][13] ==1:
             self.pc = int(self.b)
        if self.c == 768:
            if self.registre['5'][14] ==1:
                self.pc = int(self.b)
        if self.c == 1024:
            if self.registre['5'][12] ==1:
                self.pc = int(self.b)
                
        print("affichage de la memoire")
        print(self.memory)
        print("affichage des registres")
        print(self.registres)
        self.bus.mode =0
    def Clock(self):
        self.Fetch()
        self.Decode()
        self.Execute()
        
