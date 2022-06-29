import numpy as np
import matplotlib.pyplot as plt
import mpmath
from matplotlib import animation
from mpl_toolkits import mplot3d

# Number of decimal places to look
PRECISION = 72
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

points = []
numerator = int(input("Input numerator: "))
denominator = int(input("Input denominator: "))
frac = str(mpmath.fdiv(numerator, denominator))
frac = frac[2:-1]

repeats = 0
for i in range(len(frac) - 2):
    cut = frac[i:i+3]
    new = Point(int(cut[0]), int(cut[1]), int(cut[2]))

    # Check that the past 5 coordinates aren't repeated from
    # earlier in the sequence. We have to check 5 times because
    # we could escape early otherwise. For example
    # 1/980001 = 0.00000010002... This repeats '000' 3 times.
    if new in points:
        repeats += 1
        if repeats > 5:
            print(f"Period: {i - 5}")
            break
        else:
            continue
    else:
        repeats = 0

    points.append(new)

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.xlim((-0.5,9.5))
plt.ylim((-0.5,9.5))
plt.xticks(np.arange(10))
plt.yticks(np.arange(10))
plt.grid(color='gray', linestyle=':', linewidth='.2')
ax.set_title(f"Fraction: {numerator}/{denominator}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
fig.subplots_adjust(left=0.025, bottom=0.05, right=0.99, top=0.9, wspace=0.1, hspace=0)

# Plot edges
for i, j in zip(points[:-1], points[1:]):
    ax.plot3D((i.x, j.x), (i.y, j.y), (i.z, j.z), 'b', alpha=0.3)

ax.plot3D((points[0].x, points[-1].x),
        (points[0].y, points[-1].y),
        (points[0].z, points[-1].z), 'b', alpha=0.3)

# Plot start and end points.
if POINTS:
    for i, p in enumerate(points):
        ax.plot3D(p.x, p.y, p.z, 'r.', alpha=0.2)

def rotate(angle):
    ax.view_init(elev=30, azim=angle)

ani = animation.FuncAnimation(fig, rotate, frames=np.arange(0,362,2), interval=40)

mywriter = animation.FFMpegWriter(fps=20)
ani.save(f'animation_{numerator}_over_{denominator}.mp4', writer=mywriter, dpi=150)
