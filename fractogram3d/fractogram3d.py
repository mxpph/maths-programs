import numpy as np
import matplotlib.pyplot as plt
import mpmath

# Number of decimal places to look
PRECISION = 250
# Display the individual points as red dots
POINTS = True
# This is required because mpmath automatically rounds the last digit.
# We don't want that, so we calculate the next digit then cut it off.
mpmath.mp.dps = PRECISION + 1

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

def main():
    points = []
    numerator = int(input("Input numerator  : "))
    denominator = int(input("Input denominator: "))
    frac = str(mpmath.fdiv(numerator, denominator))
    # If the denominator is coprime to 10, the fraction repeats.
    if np.gcd(denominator, 10) == 1:
        frac = frac[2:-1]
    else:
        # Otherwise, it terminates, so don't cut off the last digit.
        frac = frac[2:]

    # Generate points
    for i in range(len(frac) - 2):
        cut = frac[i:i+3]
        points.append(Point(int(cut[0]), int(cut[1]), int(cut[2])))

    ax = plt.axes(projection='3d')
    plt.grid(color='gray', linestyle=':', linewidth='.2')
    ax.set_xlim((-0.5,9.5))
    ax.set_ylim((-0.5,9.5))
    ax.set_zlim((-0.5,9.5))
    ax.set_xticks(np.arange(10))
    ax.set_yticks(np.arange(10))
    ax.set_zticks(np.arange(10))
    ax.set_title(f"Fraction: {numerator}/{denominator}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Plot edges
    done = set()
    for i, j in zip(points[:-1], points[1:]):
        if (i, j) not in done:
            ax.plot((i.x, j.x), (i.y, j.y), (i.z, j.z), 'b', alpha=0.3)
            done.add((i, j))

    # Plot start and end points.
    if POINTS:
        drawn = set()
        for i, p in enumerate(points):
            if p not in drawn:
                ax.plot(p.x, p.y, p.z, 'r.' if i != 0 else 'g.',
                        alpha=(0.2 if i != 0 else 0.8))
                drawn.add(p)

    plt.show()

if __name__ == '__main__':
    main()
