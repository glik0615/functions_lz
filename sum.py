print('Введите числа через пробел')
input_list = (input())
first_list = input_list.split()
print (first_list)
my_list = list()

for i in range(0, len(first_list)):
    a = float(first_list[i])
    my_list.append(a)
print(my_list)

    
def sum(my_list):
    return 
result = my_list[0]
for i in range (1,len(my_list)):
        result = result + my_list[i]
    
print ("Сумма чисел равна", result)