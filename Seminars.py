# -------------------
# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# ----- Вариант 1 -----
'''try:
    num1 = int(input('Введите первое число - '))
    num2 = int(input('Введите второе число - '))

    if num1 == num2*num2 or num2 == num1*num1:
        print('Одно число является квадратом другого числа')
    else:
        print('Одно число не является квадратом другого числа')
except:
    print('Введите целое число')'''

# ----- Вариант 2 -----
'''try:
    num1 = int(input('Введите первое число - '))
    num2 = int(input('Введите второе число - '))

    if num1 ** 2 == num2:
        print(f'{num2} является квадратом числа {num1}')
    elif num2 ** 2 == num1:
        print(f'{num1} является квадратом числа {num2}')
    else:
        print('Ни одно число не является квадратом другого')
except:
    print('Введите целое число')'''

# -------------------
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# ----- Вариант 1 -----
'''list = []

for i in range(5):
    list.append(int(input(f'Введите {i} число - ')))

print(list)

max = list[0]

for i in range(5):
    if list[i] > max:
        max = list[i]

print(f'Максимальное число - {max}')'''

# ----- Вариант 2 -----
'''try:
    def create_list():
        list = []
        for i in range(5):
            list.append(int(input(f'Введите {i} число - ')))
        return list

    def find_max(list):
        max = list[0]

        for i in range(len(list)):
            if list[i] > max:
                max = list[i]
        return max
    
    result = create_list()
    print(result)
    max = find_max(result)
    print(f'Максимальное число - {max}')
except:
    print('Введите целое число')'''

# ----- Вариант 3 ----- + Минимальное число, макс и мин индексы, и среднее арифметическое
'''try:
    numbers = []
    for i in range(5):
        numbers.append(int(input(f'Введите число {i+1}: ')))
    max_num = numbers[0]
    min_num = numbers[0]
    index_max = 0
    index_min = 0
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        if numbers[i] > max_num:
            max_num = numbers[i]
            index_max = i
        elif numbers[i] < min_num:
            min_num = numbers[i]
            index_min = i
    print('Максимальное число =', max_num, 'Индекс = ', index_max)
    print('Минимальное число =', min_num, 'Индекс = ', index_min)
    print('Среднее арифметическое = ', sum/len(numbers))
except:
    print('Введите целое число')'''

# -------------------
#  Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# ----- Вариант 1 -----
'''try:
    def create_list(number):
        list = []
        for i in range(-number,number + 1):
            list.append(i)
        return list
   
    num = int(input(f'Введите число - '))
    result = create_list(num)
    print(result)
except:
    print('Введите целое число - ')'''

# ----- Вариант 2 -----
'''try:
    n = int(input('enter n:'))

    for i in range(-n, n + 1):
        print(i, end = ' ')
except:
    print('enter numbers')'''

# -------------------
#  Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

'''try:
    x = float(input('enter x:'))
    if int(x) - x == 0: # Проверка, если введено целое число
        print('no')
    else:
        print(int(x * 10 % 10))
except:
    print('enter numbers')'''

# -------------------
#  Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

def multiple(num):
    if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
        print("Число удовлетворяет данным условиям")
    else:
        print("Число не удовлетворяет данным условиям")
try:
    num = int(input("Введите число: "))
    multiple(num)
except:
    print('Введите целое число')