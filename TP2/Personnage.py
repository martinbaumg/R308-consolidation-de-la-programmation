class Personnage:
    def __init__(self, pseudo : str, niveau : int, nbPV : int, initiative : int):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__nbPV = nbPV
        self.__initiative = initiative
    
    def __str__(self):
        return f"Personnage {self.__pseudo} de niveau {self.__niveau} avec {self.__nbPV} points de vie et une initiative de {self.__initiative}"



    def attaque(self, joueur2):
        while self.__nbPV > 0 and joueur2.__nbPV > 0:
            self.__nbPV -= joueur2.__niveau
            print(f"Le joueur {self.__pseudo} attaque le joueur {joueur2.__pseudo} et lui inflige {joueur2.__niveau} points de dégâts !, et il lui reste {self.__nbPV} points de vie")
            joueur2.__nbPV -= self.__niveau
        if self.__nbPV <= 0:
            return 1
        elif joueur2.__nbPV <= 0:
            return 2
        else:
            return 3
    

    def soin(self):
        self.__nbPV += 1
        print(f"Le joueur {self.__pseudo} se soigne et récupère 1 point de vie ! Il lui reste {self.__nbPV} points de vie")

    
    def combat(self, joueur2):
        while self.__nbPV > 0 and joueur2.__nbPV > 0:
            result = self.attaque(joueur2)
            self.attaque(joueur2)
        if result == 1:
            print(f"Le joueur {self.__pseudo} a gagné le combat !")
        elif result == 2:
            print(f"Le joueur {joueur2.__pseudo} a gagné le combat !")

    def getPseudo(self):
        return self.__pseudo

    def getNiveau(self):
        return self.__niveau
    
    def getNbPV(self):
        return self.__nbPV
    
    def getInitiative(self):
        return self.__initiative
    
    def setPseudo(self, pseudo):
        self.__pseudo = pseudo
    
    def setNiveau(self, niveau):
        self.__niveau = niveau
    
    def setNbPV(self, nbPV):
        self.__nbPV = nbPV

    def setInitiative(self, initiative):
        self.__initiative = initiative

    def __del__(self):
        self.__pseudo = None
        self.__niveau = None 
        self.__nbPV = None
        self.__initiative = None
        print("Le personnage a été supprimé")

    

    