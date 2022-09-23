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
            print(f"Le joueur {self.__pseudo} attaque le joueur {joueur2.__pseudo} et lui inflige {joueur2.__niveau} points de dégâts !")
            joueur2.__nbPV -= self.__niveau
        if self.__nbPV <= 0:
            return 1
        elif joueur2.__nbPV <= 0:
            return 2
    

    def combat(self, joueur2):
        while self.__nbPV > 0 and joueur2.__nbPV > 0:
            result = self.attaque(joueur2)
            self.attaque(joueur2)
        if result == 1:
            print(f"Le joueur {self.__pseudo} a gagné le combat !")
        elif result == 2:
            print(f"Le joueur {joueur2.__pseudo} a gagné le combat !")
