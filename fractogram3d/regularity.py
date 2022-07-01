import numpy as np
import mpmath
from sympy import n_order, multiplicity
import pickle

# This program checks 1/2, 1/3, ..., 1/N
# for whether the edges of the fractogram
# the number creates are all the same length.

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(s, o):
        if isinstance(o, Point):
            return ((s.x == o.x)
                and (s.y == o.y)
                and (s.z == o.z))

        else: return False

    # Used for functionality with set data structure
    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash(self.__repr__())

def distance(p, q):
    return np.abs(p.x - q.x)**2 + np.abs(p.y - q.y)**2 + np.abs(p.z - q.z)**2

def main():
    regularDenoms = []
    # Dictionary to store periods of numbers 1-10000
    A007732 = pickle.load(open("A007732.p", "rb"))
    # After 1/10000, all numbers start with 0.0000
    # This means that there cannot be any more regular polygons.
    for denominator in range(2, 10000):

        period = A007732[denominator]
        if period < 3:
            continue

        mpmath.mp.dps = period + 1

        # If the denominator is coprime to 10, the fraction repeats.
        if np.gcd(denominator, 10) != 1:
            continue

        points = []
        frac = str(mpmath.fdiv(1, denominator))
        frac = frac[2:-1]

        # Generate points
        for i in range(len(frac) - 2):
            cut = frac[i:i+3]
            points.append(Point(int(cut[0]), int(cut[1]), int(cut[2])))

        done = set()
        fixdist = distance(points[0], points[1])
        for i, j in zip(points[:-1], points[1:]):
            if (i, j) in done:
                continue

            current = distance(i, j)
            if current == fixdist:
                done.add((i, j))
                continue
            else:
                break
        # Didn't break
        else:
            regularDenoms.append(denominator)

    print(regularDenoms)

if __name__ == '__main__':
    main()
