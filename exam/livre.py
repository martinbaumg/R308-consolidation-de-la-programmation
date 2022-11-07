class Livre:
    def __init__(self, recette : str, annee : int, auteur : str):
        self.__recette = recette
        self.__annee = annee
        self.__auteur = auteur
    
    def __str__(self):
        return f"Recette : {self.__recette}, Année : {self.__annee}, Auteur : {self.__auteur}"

    