print('Введите число')
number = int(input())
def check(number):
    return
for i in range(2, number):
    if number % i != 0  :
            result = " не является простым"
    elif number % i == 0 :
            result = "  является простым"
    
print ("Введенное число", check(number))