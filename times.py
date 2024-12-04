#Ввод значений
print('Введите число')
number_list = input()

#Создание списка
my_list = number_list.split('-')

#Создание списка целых чисел
first_list = list()
print(my_list)

#Преобразование типа элементов исходного спивка в integer
for i in range (0,len(my_list)):
    number = int(my_list[i])

    # Закидываем элементы преобразованного типа с новый список( после выводим его)
    first_list.append(number)
print(first_list)

#Создаем функцию, переводящую часы и минуты в секунды и в то же время суммирующую все элемнты списка(часы и минуты в секундах)
def transfer (first_list):
    return first_list[0]*3600 + first_list[1]*60 + first_list[2]

# Присваиваем значение функции некоторой переменной (закидываем туда результат)
result = transfer(first_list)

# Выводим значение
print ("Значение времени в секундах", result)