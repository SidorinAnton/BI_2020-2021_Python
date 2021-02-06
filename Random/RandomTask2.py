
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Сделайте функцию для проверки является ли список отсортированным (без использования sorted или sort).
# Затем реализуйте monkey sort,
# а потом визуализируйте следующее: распределение времени работы алгоритма от размера сортируемого списка.
# То есть по x идёт размер массива, а по y - среднее время нескольких прогонов и их отклонение (или дисперсия)


# Test if list is sorted
def is_sorted(data) -> bool:
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))


# Make bogosort O(n * n!)
def bogosort(data) -> list:
    list_to_sort = data[:]

    while not is_sorted(data=list_to_sort):
        np.random.shuffle(list_to_sort)
    return list_to_sort


# Selection sort O(n ** 2)
def selection_sort(data) -> list:
    list_to_sort = data[:]

    for i in range(len(list_to_sort)):
        min_idx = i

        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[min_idx] > list_to_sort[j]:
                min_idx = j

        list_to_sort[i], list_to_sort[min_idx] = list_to_sort[min_idx], list_to_sort[i]

    return list_to_sort


# Merge sort O (n * logn)
def merge_sort(data):
    list_to_sort = data[:]

    if len(list_to_sort) > 1:
        mid = len(list_to_sort) // 2
        L = list_to_sort[:mid]
        R = list_to_sort[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list_to_sort[k] = L[i]
                i += 1
            else:
                list_to_sort[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            list_to_sort[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list_to_sort[k] = R[j]
            j += 1
            k += 1

    return list_to_sort


# Y values
bogosort_time = np.zeros((1000, 10))  # (rows - run, cols - size of list)
selection_sort_time = np.zeros((1000, 10))
merge_sort_time = np.zeros((1000, 10))

# Make 1000 runs of every sort
for run in range(1000):  # rows, runs
    print(run)
    for i in range(10):  # col, size of list
        unsorted_list = np.random.randint(low=0, high=20, size=i)
        # print(unsorted_list)

        start_bogosort = time.time()
        bogosort(data=unsorted_list)
        bogosort_time[run][i] = time.time() - start_bogosort

        start_selection = time.time()
        selection_sort(data=unsorted_list)
        selection_sort_time[run][i] = time.time() - start_selection

        start_merge = time.time()
        merge_sort(data=unsorted_list)
        merge_sort_time[run][i] = time.time() - start_merge


# Processing data to draw
bogosort_time = pd.DataFrame(bogosort_time, index=range(1, 1001))
selection_sort_time = pd.DataFrame(selection_sort_time, index=range(1, 1001))
merge_sort_time = pd.DataFrame(merge_sort_time, index=range(1, 1001))


# Line plot
sns.lineplot(x=range(10), y=bogosort_time.mean(), label="Bogosort - O(N * N!)")
sns.lineplot(x=range(10), y=selection_sort_time.mean(), label="Selection sort - O(N ** 2)")
sns.lineplot(x=range(10), y=merge_sort_time.mean(), label="Merge sort - O(N * logN)")
plt.xticks(range(10))
plt.xlabel("Length of the sorted array")
plt.ylabel("Average time of working")
plt.legend()
plt.title("Distribution of the running time of the algorithm\non the size of the sorted list")
# plt.show()
plt.savefig("./Random_Paintings/Task2.1_bogosort.jpg", format="jpg", bb_inches="tight")
plt.close()


# Mean and points (Standard Deviation)
fig, ax = plt.subplots(1, 1)
sns.pointplot(data=bogosort_time, ci="sd", join=False, color="red")#, label="Bogosort - O(N * N!)")
sns.pointplot(data=selection_sort_time, ci="sd", join=False, color="blue")#, label="Selection sort - O(N ** 2)")
sns.pointplot(data=merge_sort_time, ci="sd", join=False, color="green")#, label="Merge sort - O(N * logN)")
ax.legend(handles=ax.lines[::10],
          labels=["Bogosort - O(N * N!)", "Selection sort - O(N ** 2)", "Merge sort - O(N * logN)"])

plt.xticks(range(10))
plt.title("Distribution of the running time of the algorithm\non the size of the sorted list")
plt.xlabel("Length of the sorted array")
plt.ylabel("Time of working (Mean and Standard deviation)")
# plt.show()
plt.savefig("./Random_Paintings/Task2.2_bogosort.jpg", format="jpg", bb_inches="tight")
plt.close()


# Mean and points (Confidence intervals)
fig, ax = plt.subplots(1, 1)
sns.pointplot(data=bogosort_time, join=False, color="red")#, label="Bogosort - O(N * N!)")
sns.pointplot(data=selection_sort_time, join=False, color="blue")#, label="Selection sort - O(N ** 2)")
sns.pointplot(data=merge_sort_time, join=False, color="green")#, label="Merge sort - O(N * logN)")
ax.legend(handles=ax.lines[::10],
          labels=["Bogosort - O(N * N!)", "Selection sort - O(N ** 2)", "Merge sort - O(N * logN)"])

plt.xticks(range(10))
plt.title("Distribution of the running time of the algorithm\non the size of the sorted list")
plt.xlabel("Length of the sorted array")
plt.ylabel("Time of working (Mean and Confidence interval)")
# plt.show()
plt.savefig("./Random_Paintings/Task2.3_bogosort.jpg", format="jpg", bb_inches="tight")
plt.close()
