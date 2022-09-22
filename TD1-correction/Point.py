import math

class Point:
    def __init__(self,x : float = 0, y : float =0 ):
        self.__x = x
        self.__y = y

    def __str__(self) -> str :
        return f"Point : x = {self.__x}, y = {self.__y}"

    def distance_coordonnees(self,x : float, y : float) -> float :
        return math.sqrt((self.__x-x)*(self.__x-x)+(self.__y-y)*(self.__y-y))

    def distance_point(self, p ) -> float:
        return math.sqrt((self.__x - p.__x) * (self.__x - p.__x) + (self.__y - p.__y)*(self.__y - p.__y))

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x : float) -> None:
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y : float) -> None:
        self.__y = y

    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False