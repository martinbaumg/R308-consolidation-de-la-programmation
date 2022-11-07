from Personnage import Personnage

def main():
    joueur1.soin()
    joueur1 = Personnage("Micha", 1, 10, 10)
    joueur2 = Personnage("Martin", 1, 10, 10)

    joueur1.combat(joueur2)

    joueur1.setPseudo("karl")

    



    


if __name__ == "__main__":
    main()