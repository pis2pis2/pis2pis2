# Тип данных МНОЖЕСТВО (set)------------------------
#------------------------------------------
     # Инициализация
temp_set = {1,2,3}
print(type(temp_set), temp_set)
temp_list = [1,2,1,2,2,3,4,12,32]
temp_set = set(temp_list)
print(type(temp_set), temp_set)
     # Обращения к элементам множества

print(100 in temp_set)

for element in temp_set:
    print(element)

     # Функции с множествами
#----------
     # Операции с множествами

     # Методы

my_set_1 = set([1, 2, 3, 4, 5])
my_set_2 = set([5, 6, 7, 8, 9])

my_set_3 = my_set_1.union(my_set_2)

print(my_set_3)

my_set_4 = my_set_1.difference(my_set_2)

print(my_set_4)