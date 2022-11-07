from Pokemon import Pokemon

def main():
    pokemon1 = Pokemon("Pikachu", "Jaune", "Vivant", 5, 80)
    pokemon2 = Pokemon("Carapuce", "Bleu", "Vivant", 3, 100)

    pokemon1.evoluer()

    pokemon2.combat(pokemon1)
 
 

if __name__ == "__main__":
    main()
   


 
    