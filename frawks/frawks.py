import numpy as np
import matplotlib.pyplot as plt
import mpmath

# Number of decimal places to look
PRECISION = 20
# Display the individual points as red dots
POINTS = False
# Label the points with the digit
LABELS = True

# This is required because mpmath automatically rounds the last digit.
# We don't want that, so we calculate the next digit then cut it off.
mpmath.mp.dps = PRECISION + 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

def main():
    points = []
    numerator = int(input("Input numerator: "))
    denominator = int(input("Input denominator: "))
    frac = str(mpmath.fdiv(numerator, denominator))
    frac = frac[2:-1]

    points.append(Point(0,0))
    for i, v in enumerate(frac):
        curDigit = int(v)
        points.append(points[i] + (np.cos(curDigit * 2 * np.pi/10), np.sin(curDigit * 2 * np.pi/10)))

    fig, ax1 = plt.subplots()
    plt.axvline(0)
    plt.axhline(0)
    ax1.set_title(f"{numerator}/{denominator}")

    # Plot edges
    for i, j in zip(points[:-1], points[1:]):
        ax1.plot([i.x, j.x], [i.y, j.y], 'b')

    # Plot start and end points.
    if POINTS:
        ax1.plot(0, 0, 'g.')
        ax1.plot(points[-1].x, points[-1].y, 'r.')

    frac = "0" + frac
    if POINTS or LABELS:
        for i, p in enumerate(points):
            if POINTS: ax1.plot(p.x, p.y, 'r.')
            if LABELS: ax1.annotate(frac[i], (p.x, p.y + 0.03), size="large")

    plt.show()

if __name__ == '__main__':
    main()
