import random

# 1. Створити список з 5 чисел, а потім вивести його у зворотному порядку.
print("завдання 1")
list_task_1 = []

for n1 in range(5):
    list_task_1.append(random.randint(1, 100))

print(list_task_1)

for i1 in range(len(list_task_1)):
    print(list_task_1[-i1 - 1], end="  ")

print()
print()

# 2. Створити список із 20 випадкових чисел. 
# Вивести всі елементи масиву з парними індексами.
print("завдання 2")

list_task_2 = []

for n2 in range(20):
    list_task_2.append(random.randint(1, 100))

print(list_task_2)

for i2 in range(1, len(list_task_2), 2):
    print(list_task_2[i2], end="  ")

print()
print()

# 3. Написати програму, яка пропонує користувачу 
# ввести число і потім підраховує, 
# скільки разів це число зустрічається 
# у списку зі 100 випадкових елементів.
print("завдання 3")

list_task_3 = []
count3 = 0
number = int(input("введіть число - "))

for n3 in range(100):
    list_task_3.append(random.randint(1, 100))

print(list_task_3)

for i3 in range(len(list_task_3)):

    if list_task_3[i3] == number:

        count3 +=1

print("Введене число зустрічається " + str(count3) + " раз")      

print()
print()

# 4. Створити список із 200 випадкових чисел
# у діапазоні від 0 до 200. 
# Визначити кількість однозначних, двозначних і тризначних
# чисел у відсотковому співвідношенні.
print("завдання 4")

list_task_4 = []

znach1 = 0
znach2 = 0
znach3 = 0

for n4 in range(200):
    list_task_4.append(random.randint(0, 200))

print(list_task_4)

for i4 in list_task_4:
    if 99 < i4 < 1000:
        znach3 += 1
    if 9 < i4 < 100:
        znach2 += 1
    if 0 <= i4 < 10:    
        znach1 += 1


print("тризначних чисел - " + str(znach3) + " або " + str(round(znach3/len(list_task_4) * 100, 2)) +" %")
print("двозначних чисел - " + str(znach2) + " або " + str(round(znach2/len(list_task_4) * 100, 2)) +" %")
print("однозначних чисел - " + str(znach1) + " або " + str(round(znach1/len(list_task_4) * 100, 2)) +" %")

print()
print()

# 5. Дано 2 списки розміром M і N відповідно. 
# Необхідно переписати у третій список 
# спільні елементи перших двох списків без повторень.

print("завдання 5")

M = int(input("введіть довжину масиву М "))
N = int(input("введіть довжину масиву N "))

list_task_m5 = []
list_task_n5 = []
list_task_5result = []

for m4 in range(M):
    list_task_m5.append(random.randint(0, 100))

for n4 in range(N):
    list_task_n5.append(random.randint(0, 100))

print("масив М")
print(list_task_m5)
print("масив N")
print(list_task_n5)
print()

for i5 in list_task_m5:
    for j5 in list_task_n5:
        if i5 == j5:
            list_task_5result.append(i5)

print("спільні елеманти двох списків: ")
print(list(set(list_task_5result)))

print()
print()

# 6. Реалізувати програму-лотерею. 
# Програма загадує 5 випадкових унікальних чисел 
# у діапазоні від 1 до 42, але не показує їх на екран. 
# Користувач намагається їх вгадати – вводить свої 5 чисел із клавіатури. 
# Призначити призи за збіги: наприклад, якщо користувач 
# вгадав три числа – приз 100 гривень, 
# якщо 4 – 500 гривень, 
# якщо 5 – 2500 гривень.
print("завдання 6")

list_lotery = []
list_numbers = []
list_lotery_result = []

print("Перевірте свою удачу в лотереї. \nВведіть 5 чисел від 1 до 42")

# введення чисел користувачем
while len(list_numbers) < 5:
    list_numbers.append(int(input("введіть номер " + str(len(list_numbers)+1) + " - ")))

print("Ваш лотерейний білет:")
print(list_numbers)

# випадкові числа лотереї без повторень 
while len(list_lotery) < 5:
    number6 = random.randint(1, 42)

    if number6 not in list_lotery:
        list_lotery.append(number6)

print("Результат лотереї:")
print(list_lotery)         

# перевірка співпадінь
for i6 in list_lotery:
    for j6 in list_numbers:
        if i6 == j6:
            list_lotery_result.append(i6)    

if len(list_lotery_result) == 3:
    print("Співпало 3 числа! Ви виграли 100 гривень!")

elif len(list_lotery_result) == 4:
    print("Співпало 4 числа! Ви виграли 500 гривень!")

elif len(list_lotery_result) == 5:
    print("Співпали всі числа! Ви виграли 50 000 гривень!")

else:
    print("Спробуйте ще, Вам обов*язково пощастить")

# 7. Створити список рядків на 3999 елементів. 
# Заповнити його римськими числами від 1 до 3999,
# показати на екрані всі елементи.

list_task7 = []
# розкладемо число на складові і складаємо в римське
for n7 in range(1, 4000):    
    s = ""

    # тисячі
    thousands = n7 // 1000
    s += 'M' * thousands

    # сотні
    hundreds = (n7 - thousands * 1000) // 100
    if hundreds == 9: s += 'CM'
    elif hundreds == 4: s += 'CD'
    elif hundreds >= 5: 
        s += 'D' + 'C' * (hundreds - 5)
    else: 
        s += 'C' * hundreds

    # десятки
    tens = (n7 - thousands * 1000 - hundreds * 100) // 10
    if tens == 9: s += 'XC'
    elif tens == 4: s += 'XL'
    elif tens >= 5: 
        s += 'L' + 'X' * (tens - 5)
    else: 
        s += 'X' * tens

    # одиниці
    ones = n7 - thousands * 1000 - hundreds * 100 - tens * 10
    if ones == 9: s += 'IX'
    elif ones == 4: s += 'IV'
    elif ones >= 5: 
        s += 'V' + 'I' * (ones - 5)
    else: 
        s += 'I' * ones

    list_task7.append(s)

for count7 in range(len(list_task7)):
    print(count7 + 1, end=" = ")
    print(list_task7[count7], end=" . ")

