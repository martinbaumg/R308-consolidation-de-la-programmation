from Animal import Animal 

def main():
    animal1 = Animal("Ta daronne", 2, 1)
    animal2 = Animal("Frimousse", 1, 1)

    animal1.vieillir()
    animal2.vieillir()

    animal1.combat(animal2)

if __name__ == "__main__":
    main()