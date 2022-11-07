from recette import Recette
from entree import Entree
from dessert import Dessert

def main():
    recette = Recette("traditionnelle", "Française", "Facile")
    entree = Entree("Salade de carrotes", "Facile")
    dessert = Dessert("Tarte aux pommes", "Facile")

    recette.concocterRecette()
    entree.concocterEntree()
    dessert.concocterDessert()

if __name__ == "__main__":
    main()