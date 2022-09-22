import sys

from Point import Point
from Cercle import Cercle
from Rectangle import Rectangle

def main():

    print("------------------Point -----------------")
    p : Point = Point()
    print (p)
    p2 : Point = Point(2,5)
    print (p2)
    distance = p2.distance_coordonnees(1,1)
    print (f"distance p2 et coordonnées 1,1 = {distance:.2f} cm")
    distance = p.distance_point(p2)
    print(f"distance p2 et point p = {distance:.2f}cm")
    print("------------------Cercle  -----------------")
    c : Cercle  = Cercle(5)
    print(f"{c} diametre {c.diametre():.2f} surface {c.surface():.2f} perimetre {c.perimetre():.2f}")
    c2 : Cercle = Cercle(centre = p2, rayon = 2)
    print(f"{c2} diametre {c2.diametre():.2f} surface {c2.surface():.2f} perimetre {c2.perimetre():.2f}")

    if (c2.intersection(c)):
        print (f"les cercles {c} et {c2} sont en intersection")
    else:
        print (f"les cercles {c} et {c2} ne sont pas en intersection")

    if (c.appartient(p2)):
        print(f"le point {p2} appartient au cercle {c}")
    else :
        print(f"le point {p2} n'appartient pas  au cercle {c}")

    print("------------------Rectangle -----------------")
    r1 : Rectangle = Rectangle()
    print (r1)

    r2 :Rectangle = Rectangle(p2,8,3)
    print(r2)
    r : Rectangle = Rectangle(p, phd = p2)
    print (r)


    print (f" {r2} a les points pbg {r2.getPointBasGauche()} pbd {r2.getPointBasDroit()} phg {r2.getPointHautGauche()} phd {r2.getPointHautDroit()}")
    p3 :Point = Point(3,5)
    if (r.appartient(p3)):
        print(f"le point {p3} appartient au rectangle {r2}")
    else :
        print(f"le point {p3} n'appartient pas au rectangle {r2}")

if (__name__ == "__main__"):
    sys.exit(main())