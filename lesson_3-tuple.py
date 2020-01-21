# Тип данных КОРТЕЖ (tuple)------------------------
#------------------------------------------
     # Инициализация
temp_list = [1,2,3]
temp_tuple = tuple(temp_list)
#temp_tuple = (1,2,3)
print(type(temp_tuple),temp_tuple)

     # Обращения к элементам кортежа
for i in range(len(temp_tuple)):
    print(temp_tuple[i])
#temp_tuple[0] = 100

     # Функции с кортежами
#-----
     # Операции с кортежами
#-----
     # Методы
#----

temp_list = [1,2,3]
temp_tuple = (1,2,3)

print(temp_list.__sizeof__())
print(temp_tuple.__sizeof__())