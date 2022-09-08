import math
class Point():
    def __init__(self, x:float = 0, y:float = 0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Point(x:{self.__x}, y:{self.__y})"

    def distance_Coordonnes(self,a:float, b:float) -> float:
        return math.sqrt((self.__x - a) * (self.__x - a) + (self.__y - b) * (self.__y - b))