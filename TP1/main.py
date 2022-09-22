import personnage as perso

def main():
    perso1 = Personnage("Jean", 100, 10)
    perso2 = Personnage("Paul", 100, 10)

    print(perso1)
    print(perso2)
    combat = perso1.combat(perso2)
    print(f"Le gagnant est {combat.get_pseudo()}")
    
    
