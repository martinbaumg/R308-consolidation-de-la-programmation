class Dessert:
    def __init__(self, nom : str, difficulte : str):
        self.__nom = nom
        self.__difficulte = difficulte

    def __str__(self):
        return f"Nom : {self.__nom}, DifficultÃ© : {self.__difficulte}"

    def concocterDessert(self):
        print("Terminons par le dessert, il s'agit d'une " + self.__nom + " qui est de difficultÃ© " + self.__difficulte)
 