# ----- ЗАДАЧА 1 ----- 
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

'''def day_of_the_week (number):
    if number > 5:
        print(f'Данный день {number} - выходной')
    else:
        print(f'Данный день {number} - является рабочим')

num = int(input('Введите цифру дня недели (1-7):'))
day_of_the_week(num)'''

# ----- ЗАДАЧА 2 -----
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

'''try:
    x = int(input("value for x: "))
    y = int(input("value for y: "))
    z = int(input("value for z: "))

    left_part = not (x or y or z)
    right_part = not x and not y and not z

    if left_part == right_part:
        print("statement is true")
    else:
        print("statement is false")
except:
    print("enter numbers!")'''


# ----- ЗАДАЧА 3 -----
# Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

'''def find_quadrant (x, y):
    if(x > 0 and y > 0): 
        print(f'Номер четверти - 1')
    elif(x < 0 and y > 0):
        print(f'Номер четверти - 2')
    elif(x < 0 and y < 0):
        print(f'Номер четверти - 3')
    elif(x > 0 and y < 0):
        print(f'Номер четверти - 4')
    else:
        print(f'Точка не имеет четверти, т.к. находится в начале координат - 0:0')

x_a = int(input('Введите координаты точки X: '))
y_a = int(input('Введите координаты точки Y: '))
quadrant = find_quadrant (x_a, y_a)'''

# ----- ЗАДАЧА 4 -----
# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

'''try:
    def calculator():
        num1 = float(input('Введите первое число - '))
        operator = (input('Введите тип операции (+, -, /, *, mod, pow, div) - '))
        num2 = float(input('Введите второе число - '))

        if operator == '+':
            res = num1 + num2
            print(f'{num1} + {num2} = {res}')
        elif operator == '-':
            res = num1 - num2
            print(f'{num1} - {num2} = {res}')
        elif operator == '*':
            res = num1 * num2
            print(f'{num1} * {num2} = {res}') 
        elif operator == 'pov':
            res = num1 ** num2
            print(f'{num1} ** {num2} = {res}')
        elif num2 != 0:
            if operator == '/':
                res = num1 / num2
                print(f'{num1} / {num2} = {res}')
            elif operator == 'mod':
                res = num1 % num2
                print(f'{num1} % {num2} = {res}')
            elif operator == 'div':
                res = num1 // num2
                print(f'{num1} // {num2} = {res}')
        else: print("Divine for zero.")

    calculator()
except:
    print('ОШИБКА! Введено не число!!! - Введите число!')'''

# ----- ЗАДАЧА 4 -----
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

def create_2d_list(m, n):
    list_2d = []
    import random
    for i in range(m):
        list = []
        for j in range(n):
            list.append(random.randint(1, 9))
        list_2d.append(list)
    return list_2d

def show_2d_list(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            print(arr_2d[i][j], end = ' ')
        print()

def sorted_2d_list(arr_2d):
    for i in range(len(arr_2d)):
        arr_2d.sort()
        for j in range(len(arr_2d[i])):
            arr_2d[i].sort()
    return arr_2d

rows = int(input('Введите колличество строк: '))
columns = int(input('Введите колличество столбцов: '))

list_2d = create_2d_list(rows, columns)

show_2d_list(list_2d)
print()
show_2d_list(sorted_2d_list(list_2d))

'''list_2d_2 = [[15,25,5,20,10], [19,24,14,4,9], [18,8,23,3,13], [12,22,2,17,7], [11,16,1,6,21]]

def show_2d_list(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            print(arr_2d[i][j], end = ' ')
        print()

def sorted_2d_list(arr_2d):
    for i in range(len(arr_2d)):
        arr_2d.sort()
        for j in range(len(arr_2d[i])):
            arr_2d[i].sort()
    return arr_2d

show_2d_list(list_2d_2)
print()
show_2d_list(sorted_2d_list(list_2d_2))'''