# Сделайте функцию-генератор,
# генерирующую все ДНКовые последовательности до длины n (аккуратно, не вызывайте её с n > 8)

# Пример вызова
# list(generate(2))
# ['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

import itertools


def generate(n):
    nucleotides = ["A", "T", "G", "C"]

    for i in range(1, n + 1):
        for sequence in itertools.product(nucleotides, repeat=i):
            yield "".join(sequence)


print(list(generate(2)))

test = ['A', 'T', 'G', 'C',
        'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

assert list(generate(2)) == test
assert list(generate(2)) == test.append("WRONG")

