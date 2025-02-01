import random

# 1.  Написати функцію draw_line, яку можна буде викликати так:
# draw_line(20, '@', true)
# і при цьому намалюється горизонтальна лінія, 
# що складається з 20 «собачок». 
# Якщо передати в останньому параметрі false — 
# лінія стане вертикальною.

def draw_line (lenth, symbol, bool):

    if bool == True:

        for i in range(lenth):
            print(symbol, end="")

    else:

        for i in range(lenth):
            print(symbol)

draw_line(5, "@", True)            

print()
print()

# 2. Написати функцію draw_rectangle, 
# яка виводить на екран прямокутник. 
# Функція приймає такі параметри: 
# ширина, висота, символ рамки, символ заповнення. 
# У функції мають бути параметри за замовчуванням.

def draw_rectangle(width=5, higth=5, border="0", background="*"):

    print(border*width)

    for i2 in range(higth-2):
        print(border,background*(width-2),border, sep="")

    print(border*width)

draw_rectangle()
print()
draw_rectangle(10,10,"-","+")

print()
print()
# 3. Написати функцію, яка перевіряє, 
# чи є передане їй число простим (і повертає True або False).
#  Число називається простим, 
# якщо воно ділиться без залишку тільки на себе і на одиницю.

def check_simple(number):

    count = 0

    for i3 in range(1, number):
        if number % i3 == 0:
            count += 1
    
    if count > 1:
        print("False")
    else:
        print("True")

check = int(input("Введіть число "))
check_simple(check)

print()
print()

# 4. Написати функцію, яка отримує як параметри 
# 2 цілі числа і повертає суму чисел із діапазону між ними.
def sum_beetween (num1, num2):
    summ=num1

    while num2 > num1:
        num1 += 1
        summ += num1

    print(summ)    

start = int(input("введіть початок діапазону "))
finish = int(input("введіть кінець діапазону "))
sum_beetween(start,finish)

print()
print()

# 5. Написати функцію, що повертає 
# середнє арифметичне елементів переданого їй списку.
def average_list(list):
    summ = 0
    print(list)

    if len(list) == 0:
        average = 0
        exit()

    for i5 in range(len(list)):
        summ += list[i5]
    average = summ / (len(list)) 

    print(average)

lenth = int(input("Введіть довжину cписку"))
average_list([random.randint(0, 100000) for j5 in range(lenth)])     

print()
print()

# 6. Написати функцію, що показує на екрані
# мінімум і максимум (значення та індекс) 
# серед елементів переданого їй списку.
def list_extremum(list):

    print(list)

    minimum = min(list)
    maximum = max(list)

    min_position = list.index(minimum) + 1
    max_position = list.index(maximum) + 1

    print("Мінімум: позиція =", min_position, "значення =", minimum)
    print("Максимум: позиція =", max_position, "значення =", maximum)

lenth = int(input("Введіть довжину cписку"))

list_extremum([random.randint(0, 100000) for j6 in range(lenth)])

print()
print()


