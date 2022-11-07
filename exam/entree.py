class Entree:
    def __init__(self, nom : str, difficulte : str):
        self.__nom = nom
        self.__difficulte = difficulte

    def __str__(self):
        return f"Nom : {self.__nom}, Difficulté : {self.__difficulte}"

    def concocterEntree(self):
        print("Commençons d'abord par l'entrée, elle est composé d'une " + self.__nom + " qui est de difficulté " + self.__difficulte)
        input("\nAppuyez sur une touche pour recevoir le dessert\n==================================================\n")

    