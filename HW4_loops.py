# #Завдання на один простий цикл while/for
# print("\nI ЗАВДАННЯ\n")
# # І завдання
# #Обчислити суму чисел в діапазоні від 1 до 10 циклом.

# number1 = 1
# sum = 0

# while number1 <= 10:
#     sum += number1
#     number1 += 1

# print (sum)

# # ІI завдання
# print("\nII ЗАВДАННЯ\n")
# #Програма виводить таблицю відповідності температур 
# #за Цельсієм і Фаренгейтом у вказаному діапазоні.

# temp_min = int(input("введіть початок діапазону "))
# temp_max = int(input("введіть кінець діапазону "))

# if temp_min > temp_max: 
#     print("невірно заданий діапазон")
#     exit()

# print(" C     F  ")

# while temp_min <= temp_max:
#     print("────────────")
#     print(temp_min, end=(" │ "))
#     print(round(temp_min * 1.8 + 32, 2))
#     temp_min += 1

# print("────────────")

# # ІII завдання
# print("\nIII ЗАВДАННЯ\n")

# #Загадати випадковим чином 100 цілих чисел 
# #у діапазоні від -100 до 100. 
# #Обчислити відсоток позитивних чисел, 
# #відсоток негативних чисел і відсоток нулів, 
# #а також парних чисел і відсоток непарних.

# import random

# count = 1
# positive = 0
# negative = 0
# zero = 0
# parni = 0
# neparni = 0

# while count <= 100:
#     number = random.randint(-100, 100)
#     print(number, end=(", "))
#     if number > 0:
#         positive += 1
#     elif number < 0:
#         negative += 1
#     else: zero += 1

#     if number % 2 == 0:
#         parni += 1
#     else: neparni +=1

#     count += 1

# print("\nвідсоток позитивних - " + str(positive) + " %")
# print("відсоток негативних - " + str(negative) + " %")
# print("відсоток нулів - " + str(zero) + " %")
# print("відсоток парних - " + str(parni) + " %")
# print("відсоток непарних - " + str(neparni) + " %")

# # ІV завдання
# print("\nIV ЗАВДАННЯ\n")
# #Написати програму, яка обчислює факторіал введеного числа.

# number_fact = int(input("введіть ціле невід\'ємне число "))
# start = 1
# result = 1

# if number_fact == 0:
#     print("0! = 1")
#     exit("")
# if number_fact < 0:
#     print("Число від\'ємне")
#     exit("")

# while start <= number_fact:
#     result *= start
#     start += 1

# print(str(number_fact) + "! = " + str(result))

# # V завдання
# print("\nV ЗАВДАННЯ\n")
# # З клавіатури вводиться ціле число будь-якої розрядності. 
# # Визначити кількість цифр у ньому та їхню суму.

# number5_task = int(input("Введіть ціле число "))
# digit_sum = 0 # початкове значення суми цифр
# digit_count = 0 #початкове значення лічильника

# while number5_task != 0:
#     digit_sum += number5_task % 10
#     number5_task //= 10
#     digit_count += 1

# print("Кількість цифр = " + str(digit_count))
# print("Сума цифр = " + str(digit_sum))

# VІ завдання
# print("\nVІ ЗАВДАННЯ\n")
# З клавіатури вводиться ціле число. 
# Вивести на екран всі числа, 
# на які введене число ділиться без залишку.

# number6_task = int(input("Введіть ціле число "))
# digit_div = 1

# print("введене число ділиться без залишку на: ")

# while digit_div <= number6_task:
    
#     if number6_task % digit_div == 0:
#         print (digit_div, end=(", "))

#     digit_div += 1    

# # VІІ завдання
# print("\nVІІ ЗАВДАННЯ\n")
# # З клавіатури вводиться ціле число. 
# # Визначити, чи є воно простим. 
# # Просте число ділиться без залишку 
# # лише на 1 і на саме себе.
# number7_task  = int(input("Введіть ціле число "))
# digit7_div = 1
# count = 0

# while digit7_div < number7_task:

#     if number7_task % digit7_div == 0:
#         count += 1

#     digit7_div += 1

# if count > 1:
#     print("введене число - не є простим")

# else:
#     print("введене число є простим")


# # IIX завдання
# print("\nIIX ЗАВДАННЯ\n")
# # Перевірити, чи є в введеному числі 
# # однакові цифри підряд.
# number8_task = int(input("введіть просте число "))
# digit1 = 0
# digit2 = 0

# while number8_task != 0:
#     digit1 += number8_task % 10
#     number8_task //= 10
#     if digit2 == digit1:
#         print("У введеному числі є однакові цифри підряд")
#         exit("")
#     digit2 += number8_task % 10
#     number8_task //= 10
#     if digit2 == digit1:
#         print("У введеному числі є однакові цифри підряд")
#         exit("")

# print("У введеному числі немає однакових цифр підряд")        


# #Завдання на псевдографіку

# #1. Показати на екрані рівнобедрений трикутник висотою N.
# print("\nI ЗАВДАННЯ\n")

# size = int(input("rozmir "))

# for i in range(0, size):
#     for j in range(0, size):
#         print(end=" ")
#     size -= 1  
#     for j in range(0, i + 1):
#         #print("⓿", end=' ')
#     print(" ")


# print("\nV ЗАВДАННЯ\n")
# #5*. Ялинка зi слайду в кiнцi презентації.

# import os
# os.system('cls')
# a = 9 
# for b in range (3):
#     size = a
    
#     for i in range(0, size):
        
#         for j in range(0, size):
#             print(end=" ")
#         size -= 1 
    
#         for j in range(0, i + 1):
#             print("●", end=' ')
#         print(" ")

# size = int(a / 2)

# for b in range(size + 1):

#     for i in range(size + 1):
#             print(end=" ")

#     for j in range(size + 1):
#        print("*", end=(" "))
       
#     print()

# input()


# #Завдання на вкладені цикли:

# #Написати програму, що показує таблицю множення
# print("\nI ЗАВДАННЯ\n")
# mnoj_1 = 0 #І множник

# while mnoj_1 <= 8:
#     print()
#     print(mnoj_1 + 1)
#     print()
#     mnoj_1 += 1
#     mnoj_2 = 1 #ІІ множник

#     while mnoj_2 <= 9:
#         print(str(mnoj_1) + " * " + str(mnoj_2) + " = ", end=(""))
#         print(mnoj_1 * mnoj_2)
#         mnoj_2 += 1

## Показати номери та загальну кількість усіх 
## щасливих трамвайних квитків з шестизначними номерами.   
 
# print("\nII ЗАВДАННЯ\n")

# n1 = 0
# ticket = 0
# while n1 <= 9:
#     n6 = 0

#     while n6 <= 9:
#        n2 = 0

#        while n2 <=9:
#             n5 = 0

#             while n5 <=9:
#                 n3 = 0

#                 while n3 <= 9:
#                     n4 = 0

#                     while n4 <= 9:

#                         if n1+n2+n3 == n4+n5+n6:
#                             print(n1, n2, n3, n4, n5, n6)
#                             ticket += 1
#                         n4 +=1                            

#                     n3 += 1    

#                 n5 += 1    

#             n2 += 1    

#        n6 += 1 

#     n1 += 1             

# print(ticket)

# Написати програму, яка генерує і виводить 
# календар на будь-який рік, вказаний з клавіатури.
print("\nVII ЗАВДАННЯ\n")

import os
os.system('cls')

size = 7
year = int (input("Введіть рік "))
month = 1

for month in range (1, 13):
    #розрахунок І дня кожного місяця
    year_calc = year
    month_calc = month
    day = 1    

    if month == 1 or month == 2:  # Січень і Лютий розглядаються як 13 і 14 місяці попереднього року
        month_calc += 12
        year_calc -= 1

    h = (day + (13 * (month_calc + 1)) // 5 + year_calc % 100 + ((year_calc % 100) // 4) +
          ((year_calc // 100) // 4) - (2 * (year_calc // 100))) % 7
    if 2 <= h <= 6:
        space = h-2
    else: space = h + 5    

    print()
    print("  ====== ", end='')
    print(month, end='')
    print(" ======")
    print("пн вт ср чт пт сб нд")
        
    if (month == 1 or month == 3 or 
            month == 5 or month == 7 or
            month == 8 or month == 10 or 
            month == 12):
        for b in range(size):
            if day == 1:
                  for i in range(space):
                        print("   ", end='')
                 
            if day > 31: break
           
            for w1 in range(space, size):                                                
                if day < 10:                        
                    print(day, end=("  "))                
                else: print(day, end=(" "))                
                day += 1                
                if day + space > 8: break

            print()    

            for w2 in range(size - 1):
                if day > 31: break                                
                if day < 10:                        
                    print(day, end=("  "))                
                else: print(day, end=(" "))                
                day += 1             

    elif (month == 4 or month == 6 or 
            month == 9 or month == 11):
        for b in range(size):
            if day == 1:
                  for i in range(space):
                        print("   ", end='')
                 
            if day > 30: break
           
            for w1 in range(space, size):                                                
                if day < 10:                        
                    print(day, end=("  "))                
                else: print(day, end=(" "))                
                day += 1                
                if day + space > 8: break

            print()    

            for w2 in range(size - 1):
                if day > 30: break                                
                if day < 10:                        
                    print(day, end=("  "))                
                else: print(day, end=(" "))                
                day += 1

    else:
        if (year % 4 == 0 and 
            year % 100 != 0) or year % 400 == 0:
            for b in range(size):
                if day == 1:
                  for i in range(space):
                        print("   ", end='')
                 
                if day > 29: break
            
                for w1 in range(space, size):                                                
                    if day < 10:                        
                        print(day, end=("  "))                
                    else: print(day, end=(" "))                
                    day += 1                
                    if day + space > 8: break

                print()    

                for w2 in range(size - 1):
                    if day > 29: break                                
                    if day < 10:                        
                        print(day, end=("  "))                
                    else: print(day, end=(" "))                
                    day += 1
                  
        else:
            for b in range(size):
                if day == 1:
                  for i in range(space):
                        print("   ", end='')
                 
                if day > 28: break
            
                for w1 in range(space, size):                                                
                    if day < 10:                        
                        print(day, end=("  "))                
                    else: print(day, end=(" "))                
                    day += 1                
                    if day + space > 8: break

                print()    

                for w2 in range(size - 1):
                    if day > 28: break                                
                    if day < 10:                        
                        print(day, end=("  "))                
                    else: print(day, end=(" "))                
                    day += 1
input()
