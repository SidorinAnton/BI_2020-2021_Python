import numpy as np
import matplotlib.pyplot as plt

# Сгенерируйте и нарисуйте коврик Серпинского


def midpoint(p, q):
    return [(p[0] + q[0]) / 3, (p[1] + q[1]) / 3]


side = [(0, 1), (1, 0), (1, 2), (2, 1),
        (0, 0), (2, 0), (0, 2), (2, 2)]

n = 1000000
x = np.zeros(n)
y = np.zeros(n)

val = np.random.randint(low=0, high=8, size=n)

for i in range(1, n):
    k = val[i - 1]
    x[i], y[i] = midpoint(side[k], (x[i - 1], y[i - 1]))

plt.scatter(x, y, alpha=0.6)
plt.title("Sierpinski carpet")
plt.savefig("./Random_Paintings/Task6_Sierpinski_carpet.jpg", format="jpg", bb_inches="tight")
# plt.show()
plt.close()