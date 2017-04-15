# module Memoire
import 04-04-Memoire
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
    bus = None          # bus
    pc=0                # program counter - contient l'adresse de la prochaine instruction
    code= []            # instruction to execute
    alu = None          # ALU
    lines =[]           # instructions du rom
    a=0                 # instruction
    b=0                 # valeur 1
    c=0                 # code de l'operation 2
    d =0                # registre à utiliser
    regA=0              # registre A
    regB=0              # registre B
    regC=0              # registre C
    regD=0              # registre D
    Status=[16]         # registre de Status
    memory=None         # memoire
    critic =0           # condiiton d'arret d'execution
    ram ={}             # ram
    rom{}               # rom
    io={}               # io
    

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
        self.alu = alu(bus)
        self.memory = Memoire(bus,self.ram,self.io,self.rom)
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
            Cette fonction permet d'aller chercher l'instruction se trouvant à l'adresse se trouvant dans
            self.pc.Elle fait intervenir le bus
        """
        print("FETCH")
        #print("Coup d'horloge")
        self.bus.mode = 2
        #print("self.bus.mode = ",self.bus.mode)
        #print("Le bus est en mode Read")
        #print("on va cherhcer l'instruction à executer et on la met dans self.code")
        self.bus.data = lines[self.pc].split()
        self.code = self.bus.data
        #print("instruction = ",self.code)
        #print("on met le bus en mode inerte")
        self.bus.mode = 0
        #print("on incrémente pc")
        self.pc = self.pc+1
      
    def Decode(self):
          print("DECODE")
          
          if len(self.code)==2:
                self.a=int(self.code[0])  # a ccnserve l'instruction
                self.b=self.code[1]  # b contient la valaur a modifier
                self.c=(self.a & 65280) # code de l'operation
                self.d = (self.a & 15) # registre à considerer dans le cas d'un stranfert
          if len(self.code)==1:
                self.a=int(self.code[0]) # a ccnserve l'instruction
                self.c=(self.a & 65280) # code de l'operation 
            
          if self.c in [4352,4608,4864,5120]:
                print("operation de l'alu")
                
          if self.c not in [4352,4608,4864,5120]:
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
          print("EXECUTE")
          if self.c==4352:
                value1 =self.registres[str(self.d)]
                value2 =self.registres[str(self.b)]
                x=alu.fonctionADD(value1,value2)
                if(x>65535):
                      self.registres['5'][14] = 1
                self.registres[str(self.d)]=x
                if(x<0):
                      self.registres['5'][15] = 1
          if self.c==4608:
                value1 =self.registres[str(self.d)]
                value2 =self.registres[str(self.b)]
                x=alu.fonctionSUB(value1,value2)
                if(x<0):
                      self.registres['5'][15] = 1
                if(x>65535):
                      self.registres['5'][14] = 1
                self.registres[str(self.d)]=x
          if self.c==4864:
                value1 =self.registres[str(self.d)]
                value2 =self.registres[str(self.b)]
                x=alu.fonctionMUL(value1,value2)
                if(x>65535):
                      self.registres['5'][14] = 1
                if(x<0):
                      self.registres['5'][15] = 1
                self.registres[str(self.d)]=x
          if self.c==5120:
                value1 =self.registres[str(self.d)]
                value2 =self.registres[str(self.b)]
                x=alu.fonctionDIV(value1,value2)
                if(x>65535):
                      self.registres['5'][14] = 1
                if(x<0):
                      self.registres['5'][15] = 1
                self.registres[str(self.d)]=x
          
          
          if self.c==1280:
                self.registres[str(self.d)] = int(self.code[1])
          if self.c==1792 or self.c==1536:
                self.memory.setMemory(self.b,int(self.bus.data))
          if self.c ==2048:
                self.registres[str(self.d)] = self.memory.getMemory(self.b)
          if self.c==8448:
                print(" or binaire")
                x = self.registres[str(self.d)]|self.registres[str(self.b)]
                self.registres[str(self.d)]= x
          if self.c==8704:
                print(" AND binaire")
                x = self.registres[str(self.d)]&self.registres[str(self.b)]
                self.registres[str(self.d)]= x
          if self.c==8960:
                print(" AND binaire")
                x = self.registres[str(self.d)]^self.registres[str(self.b)]
                self.registres[str(self.d)]= x
          if self.c==9216:
                print("la fonction NOT")
                x = ~self.registres[str(self.d)]& 65535
                self.registres[str(self.d)]= x
                
                
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
          if self.c == 3840:
                self.critic=1
                print("arret d'execution a cause de l'instruction HALT ")
      
                
          #print("affichage de la memoire")
          #print(self.memory)
          #print("affichage des registres")
          #print(self.registres)
          #self.bus.mode =0
          
    def Clock(self):
        self.Fetch()
        self.Decode()
        self.Execute()
        
