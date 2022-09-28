class Animal:
    def __init__(self, nom : str, age : int, pv : int):
        self.__nom = nom
        self.__age = age 
        self.__pv = pv

    def __str__(self):
        return f"Animal {self.__nom} de {self.__age} ans"

    def vieillir(self):
        while self.__age < 10:
            self.__age += 1
            print(f"{self.__nom} a grandit, elle a mainteannt {self.__age} ans")
        if self.__age == 10:
            print(f"{self.__nom} est assez grande pour combattre")
            return 1

    def attaque(self, animal2):
        while self.__pv > 0 and animal2.__pv > 0:
            self.__pv -= 1
            print(f"{self.__nom} attaque {animal2.__nom} et lui inflige {animal2.__age} points de dégâts !, et il lui reste {self.__pv} points de vie")
            animal2.__pv -= 1
        if self.__pv <= 0:
            return 1
        elif animal2.__pv <= 0:
            return 2
        else:
            return 3

    def combat(self, animal2):
        print(f"le combat entre {self.__nom} et {animal2.__nom} commence")
        while self.__pv > 0 and animal2.__pv > 0:
            result = self.attaque(animal2)
            self.attaque(animal2)
        if result == 1:
            print(f"{self.__nom} a gagné le combat !")
        elif result == 2:
            print(f"{animal2.__nom} a gagné le combat !")