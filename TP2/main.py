from Personnage import Personnage

def main():
    joueur1 = Personnage("Joueur 1", 10, 10, 10)
    joueur2 = Personnage("Joueur 2", 1, 10, 10)

    joueur1.combat(joueur2)

if __name__ == "__main__":
    main()