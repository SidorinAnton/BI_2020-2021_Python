
import numpy as np
import pylab
import seaborn as sns
import matplotlib.pyplot as plt


# Визуализируйте random walk в 2-мерном пространстве,
# где вы начинаете в (0, 0) и можете перемещаться вверх, вниз, вправо и влево.
# Как визуализировать - скаттерплот, где по x - x, а по y - y


n = 100000

x = np.zeros(n)
y = np.zeros(n)

for i in range(1, n):
    val = np.random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1



pylab.title(f"Random Walk with pylab ($n$ = {n} steps)")
pylab.plot(x, y)
pylab.grid()
pylab.savefig("./Random_Paintings/Task3.1_random_walk.jpg", format="jpg", bb_inches="tight")
# pylab.show()
pylab.close()



sns.scatterplot(x=x, y=y)
plt.title(f"Random Walk with seaborn ($n$ = {n} steps)")
plt.grid()
# plt.show()
plt.savefig("./Random_Paintings/Task3.2_random_walk.jpg", format="jpg", bb_inches="tight")
plt.close()
