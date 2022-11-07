class Pokemon:
    def __init__(self, nom : str, couleur : str, etat : str, niveau : int, pv : int):
        self.__nom = nom
        self.__couleur = couleur
        self.__etat = etat
        self.__niveau = niveau
        self.__pv = pv

    def __str__(self):
        return f"Nom : {self.__nom}, Couleur : {self.__couleur}, Etat : {self.__etat}, Niveau : {self.__niveau}, PV : {self.__pv}"

    def evoluer(self):
        self.__niveau += 1
        print(f"-------------------------------------------------\n{self.__nom} a évolué ! Il est maintenant niveau {self.__niveau}.\n-------------------------------------------------")
        self.__pv += 10
        print(f"{self.__nom} a augmenté de niveau donc il a gagné 10 PV, il a donc désormais {self.__pv} PV.")


    def combat(self, pokemon):
        if self.__etat == "Vivant":
            print(f"{self.__nom} attaque {pokemon.__nom} !\n")
            pokemon.attaquer()
        else:
            print(f"{self.__nom} est mort, il ne peut pas attaquer !")


    def attaquer(self):
        while self.__pv > 0:
            self.__pv -= 10
            print(f"{self.__nom} a perdu 10 PV ! Il lui reste {self.__pv} PV.")
        else:
            self.__etat = "Mort"
            print(f"{self.__nom} est mort !")



    
        

        
        



  

