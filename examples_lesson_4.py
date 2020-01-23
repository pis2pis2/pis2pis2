
import random
  # 20 имен
list_names = ['Pavel','Rita','Arsen','Jorik','Artem','Oleg','Tanya','Olga','Kate','Anna','Kirill','Pavel','Rita','Arsen','Jorik','Artem','Oleg','Tanya','Olga','Kate','Anna']
print(list_names,type(list_names))

def f(list_names,n):
    list_names_random = []
    len_list = len(list_names)

    for i in range(1, n + 1):
            # randomChoice - это случайное число в пределах длины начального списка,
            # случайным образом выбираем индекс
            randomChoice = random.randint(0, len_list-1)
            # newName - это случайное слово по индексу
            newName = list_names[randomChoice]
            # Добавляем случайное слово newName в список
            list_names_random.append(newName)

    return list_names_random

# print(f(list_names,25))
list_names_random = f(list_names,50)
print (list_names_random)
#
# import random
#
# print()
# print("Задача 1. \nВыбор 100 случайных имен из списка")
# # 20 имен
# list_names = ['Pavel','Rita','Arsen','Jorik','Artem','Oleg','Tanya','Olga','Kate','Anna','Kirill','Pavel','Rita','Arsen','Jorik','Artem','Oleg','Tanya','Olga','Kate']
#
#
# def name_n(list_names, n):
#     '''
#     :param list_names: список имен
#     :param n: длина списка на выходе
#     :return: список из 20 случайных имен
#     '''
#     list_names_random = []
#     len_list = len(list_names)
#     newName = ''
#
#     for i in range(1, n + 1):
#         # randomChoice - это случайное число в пределах длины начального списка,
#         # случайным образом выбираем индекс
#         randomChoice = random.randint(0, len_list-1)
#         # newName - это случайное слово по индексу
#         newName = list_names[randomChoice]
#         # Добавляем случайное слово newName в список
#         list_names_random.append(newName)
#
#     return list_names_random
#
# list_names_random = name_n(list_names, 50) # n == 100
# print('Список: \n%s\nКоличество слов: %s\nИзначально слов: %s' % (list_names_random, len(list_names_random), len(list_names)))
# print()