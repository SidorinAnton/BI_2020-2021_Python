import matplotlib.pyplot as plt
import pandas as pd

# В файлике train.csv содержится информация о числе ридов с каждым из 4-ёх нуклеотидов по разным позициям
# (колонки A, T, G, C)). Постройте гистограмму распределения этих чисел
# По x должны идти позиции (pos), а по y - частота для каждой из букв (stacked barplot)

train = pd.read_csv(
    "https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv"
)

nucleotide_data = train.loc[:, ["A", "C", "T", "G"]]


# Make a plot
nucleotide_data.plot.bar(stacked=True, figsize=(20, 10))

plt.xticks(ticks=train.index, labels=train.pos)
plt.xlabel("Position in reads")
plt.ylabel("Frequency of nucleotide")
# plt.show()
plt.savefig("../1.Histogram_task.jpg", format="jpg", bb_inches="tight")
plt.close()
