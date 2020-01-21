# # # Тип данных СЛОВРИ (dict)------------------------
# # #------------------------------------------
# #      # Инициализация
# # dict_temp = {}
# #
# # print(type(dict_temp), dict_temp)
#
# # dict_temp = {'dict1': 1, 'dict2': 2.1, 'dict3': 'name', 'dict4':[1,2,3]}
# # print(type(dict_temp), dict_temp)
# #
# # dict_temp = dict.fromkeys(['a', 'b'], [12,'2020'])
# # print(type(dict_temp), dict_temp)
# #
# # dict_temp = dict(brend = 'volvo', volume_engine = 1.5)
# #
# # print(type(dict_temp), dict_temp)
# #
# dict_temp = {a: a**2 for a in range(10)}
# print(type(dict_temp), dict_temp)
# #      # Обращения к содержимому словаря
# #
# # print(dict_temp[8])
# #
# #      # Функции со словарями
# #
# print(list(dict_temp.keys()))
# print(list(dict_temp.values()))
# #
# print(list(dict_temp.items()))
# #
# #      # Работа с элементами
# # dict_temp[0] = 100
# # print(type(dict_temp), dict_temp)
# #
# # dict_temp['name'] = 'Dima'
# # print(type(dict_temp), dict_temp)
# #
# #      # Методы
# # # keys, values, items см выше
# #
# # temp = dict_temp.pop('name')
# # print(temp)
# # print(type(dict_temp), dict_temp)
# #
# #
# # # Итерирование по словарю
# # for pair in dict_temp.items():
# #     print(pair)
# #
# # for key, value in dict_temp.items():
# #     print(key, value)
# #
# # for key in dict_temp.keys():
# #     print(key)
# #
# # for value in dict_temp.values():
# #     print(value)