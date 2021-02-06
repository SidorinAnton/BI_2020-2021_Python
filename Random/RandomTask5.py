
import numpy as np
import random

# Сделайте программу, получающую на вход текст, и выдающую этот же текст со следующими изменениями -
# буквы во всех словах кроме первой и последней перемешаны.
# Для простоты пока будем считать, что пунктуации нет.


text = input().split()


# For test
# test_string = '''По результатам исследования одного английского университета
# не имеет значения в каком порядке расположены буквы в слове
# Главное чтобы первая и последняя буквы были на месте
# Остальные буквы могут следовать в полном беспорядке
# все равно текст читается без проблем
# Причиной этого является то что мы не читаем каждую букву отдельно
# а всё слово целиком'''
#
# text = test_string.split()


changed_text = []

for word in text:
    middle_to_change = list(word[1:-1])
    np.random.shuffle(middle_to_change)
    new_word = word[0] + "".join(middle_to_change) + word[-1] if len(word) != 1 else word
    changed_text.append(new_word)

print(" ".join(changed_text))

