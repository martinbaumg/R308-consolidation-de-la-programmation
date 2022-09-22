class Personnage :
    def __init__(self, pseudo : str, niveau : int = 1, nbPv : int = 1, initiative : int = 5):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__nbPv = niveau
        self.__initiative = niveau
    
    def __str__(self) -> str:
        return f"Personnage {self.__pseudo} de niveau {self.__niveau} avec {self.__nbPv} points de vie et une initiative de {self.__initiative}"

    def comnbat(self,autrepersonnage):
        if self.__initiative > autrepersonnage.__initiative:
            return self
        else:
            return autrepersonnage
    
    def mort(self):
        if self.__nbPv <= 0:
            return True
        else:
            return False
    
    def attaque(self,autrepersonnage):
        if self.mort() == False:
            autrepersonnage.__nbPv -= 1
        else:
            print("Le personnage est mort")
    
    def soin(self):
        if self.mort() == False:
            self.__nbPv += 1
        else:
            print("Le personnage est mort")
    
    def get_pseudo(self):
        return self.__pseudo

    def get_niveau(self):
        return self.__niveau
    
    def get_nbPv(self):
        return self.__nbPv