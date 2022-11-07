class Auteur: 
    def __init__(self, nom : str, prenom : str, livre : str):
        self.__nom = nom
        self.__prenom = prenom
        self.__livre = livre

    def __str__(self):
        return f"Nom : {self.__nom}, Prénom : {self.__prenom}, Livre : {self.__livre}"

    