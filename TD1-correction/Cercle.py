from Point import Point
import math

class Cercle:
    def __init__(self, rayon : float, centre : Point = None):
        self.__rayon  = rayon
        if centre == None:
            self.__centre = Point(0,0)
        else:
            self.__centre = centre

    def __str__(self) -> str:
        return f"Cercle de centre {self.__centre} et de rayon {self.__rayon}"

    def diametre(self) -> float:
        return self.__rayon* 2

    def perimetre(self) -> float :
        return self.diametre()*math.pi

    def surface(self) -> float:
        return math.pi*self.__rayon*self.__rayon

    def intersection(self,autrecercle) -> bool:
        res : bool = False
        if self.__centre.distance_point(autrecercle.__centre) < self.__rayon+autrecercle.__rayon:
            res=True
        return res

    def appartient(self,p : Point) -> bool :
        if self.__centre.distance_point(p) < self.__rayon:
            return True
        else:
            return False

