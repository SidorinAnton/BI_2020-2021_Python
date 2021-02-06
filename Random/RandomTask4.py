
import numpy as np
import matplotlib.pyplot as plt

# Сгенерируйте и нарисуйте треугольник Серпинского


def midpoint(p, q):
    return [0.5 * (p[0] + q[0]), 0.5 * (p[1] + q[1])]


n = 100000
point = [0, 0]

v1 = [0, 0]
v2 = [1, 0]
v3 = [0.5, 0.5 * 3 / 2]

val = np.random.randint(low=0, high=3, size=n)

for i in val:
    if i == 0:
        point = midpoint(point, v1)
    elif i == 1:
        point = midpoint(point, v2)
    elif i == 2:
        point = midpoint(point, v3)

    plt.plot(point[0], point[1], "m.", markersize=3)

plt.title("Sierpinski triangle")
plt.savefig("./Random_Paintings/Task4_Sierpinski_triangle.jpg", format="jpg", bb_inches="tight")
# plt.show()
plt.close()
