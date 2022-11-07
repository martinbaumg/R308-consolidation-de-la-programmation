class Recette:
    def __init__(self, nom : str, origine : str, difficulte : str):
        self.__nom = nom
        self.__origine = origine
        self.__difficulte = difficulte

    def __str__(self):
        return f"Nom : {self.__nom}, Origine : {self.__origine}, Difficulté : {self.__difficulte}"


    def concocterRecette(self):
        print("\nJe vais concocter la recette de " + self.__nom + " qui est de difficulté " + self.__difficulte + " et qui est originaire de " + self.__origine)
        input("\nAppuyez sur une touche pour recevoir l'entrée \n============================================\n")


   