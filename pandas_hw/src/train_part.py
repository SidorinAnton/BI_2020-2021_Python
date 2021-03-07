import pandas as pd

# Сохраните в файл train_part.csv следующую часть из файла train.csv:
# строки, где matches больше чем среднее колонки pos, reads_all, mismatches, deletions, insertions


train = pd.read_csv(
    "https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv"
)

mean_matches = train.matches.mean()

train_part = train.query("matches > @mean_matches")[
    ["pos", "reads_all", "mismatches", "deletions", "insertions"]
]


train_part.to_csv("../2.train_part.csv")
