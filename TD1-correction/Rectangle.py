from Point import Point

class Rectangle :
    def __init__(self,pbg : Point = Point(0,0), longueur : float = 1, hauteur : float = 1, phd : Point = None):
        self.__pointBasGauche = pbg
        self.__longueur = longueur
        self.__hauteur = hauteur
        if phd != None:
            self.__longueur = phd.get_x() - pbg.get_x()
            self.__hauteur = phd.get_y() - pbg.get_y()

    def __str__(self) -> str:
        return f"Rectangle de point bas gauche {self.__pointBasGauche}, de longueur {self.__longueur} et de hauteur {self.__hauteur}"

    def surface(self) -> float:
        return self.__hauteur * self.__longueur

    def perimetre(self) -> float :
        return 2 * (self.__longueur + self.__hauteur)

    def getPointBasGauche(self) -> Point:
        return self.__pointBasGauche

    def getPointBasDroit(self) -> Point:
        p : Point = Point (self.__pointBasGauche.x+self.__longueur,self.__pointBasGauche.y)
        return p

    def getPointHautDroit(self) -> Point:
        p : Point = Point (self.__pointBasGauche.x+self.__longueur,self.__pointBasGauche.y+self.__hauteur)
        return p

    def getPointHautGauche(self) -> Point:
        p : Point = Point (self.__pointBasGauche.x,self.__pointBasGauche.y+self.__hauteur)
        return p

    def appartient(self,p : Point) -> bool :
        res = False
        if   self.__pointBasGauche.x+self.__longueur > p.x > self.__pointBasGauche.x  and self.__pointBasGauche.y+self.__hauteur > p.y > self.__pointBasGauche.y:
            res = True
        return res
