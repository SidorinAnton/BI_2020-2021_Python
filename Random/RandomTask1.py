
import numpy as np
import random
import time
import matplotlib.pyplot as plt
import seaborn as sns


# Task 1
# Замерьте время вычисления чисел от 0 до 1 из равномерного распределения с помощью модуля random и модуля numpy,
# изобразите зависимость времени вычисления от количества вычисляемых чисел для них.
# Другими словами - по x идёт то, сколько чисел за прогон вы взяли от 0 до 1, а
# по y - время, которое это заняло. И сравните время выполнения в numpy и в random)


def time_of_libs_random(number_of_times: int) -> tuple:
    # Random
    start_random = time.time()
    for _ in range(number_of_times):
        random.randint(0, 1)
    end_random = time.time()

    # Numpy
    start_numpy = time.time()
    np.random.uniform(0, 1, size=number_of_times)
    end_numpy = time.time()

    return end_random - start_random, end_numpy - start_numpy


random_time = np.zeros(10 ** 4)
numpy_time = np.zeros(10 ** 4)

print("Go")
for i in range(0, 10 ** 4):
    value = time_of_libs_random(i)
    random_time[i] = value[0]
    numpy_time[i] = value[1]
print("Done")

sns.lineplot(x=range(0, 10**4), y=random_time, label="random lib")
sns.lineplot(x=range(0, 10**4), y=numpy_time, label="numpy lib")
plt.xlabel("Number of random values")
plt.ylabel("Time of working")
plt.legend()
# plt.show()
plt.savefig("./Random_Paintings/Task1_random_vs_numpy.jpg", format="jpg", bb_inches="tight")
plt.close()
