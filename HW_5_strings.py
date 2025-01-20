import random 
import string
import re

# 1. Підрахувати середню довжину слова у введеному реченні.

sentence = str(input("Enter text - "))
space_count = 1

for letter in sentence:
    if letter == " ":
        space_count += 1

av_word_len = (len(sentence) + 1 - space_count) / (space_count)      

print("Середня довжина слова в реченні становить ", end="")
print(av_word_len)

# 2. Підрахувати, скільки разів певне слово міститься в рядку тексту.

text_string = str(input("Enter text - "))
wanted_word = str(input("Enter wanted word - "))
count_word = text_string.count(wanted_word)

if count_word > 0:
    print("Дане слово зустрічається в реченні стільнки разів")
    print(count_word)
else: print("Дане слово не зустрічається в реченні")    

# 3. Напишіть програму, яка генерує пароль вказаної довжини.

pass_lenth = int(input("Введіть довжину пароля "))
genrated_password = ""
x = 0

while x < pass_lenth:

    genrated_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    x +=1

print("Згенерований пароль:")
print(genrated_password)    
    

# 4. Визначити, яка буква в тексті зустрічається найчастіше.

text_task4 = str(input("Enter text - "))
text_task4 = text_task4.lower()

#припустимо що найчастіше зустрічається перша літера
letter_max = text_task4[0]
count_max = text_task4.count(letter_max) 

n=0

#порівнюємо з наступною і заміняємо в разі необхідності
while n < len(text_task4):
    
    if text_task4.count(text_task4[n]) > count_max:

        letter_max = text_task4[n]
        count_max = text_task4.count(text_task4[n])

    n += 1    

print("найчастіше зустрічається:")
print(letter_max)
print("у кількості:")
print(count_max)

# 5. Написати програму, яка перевіряє коректність email, вказаного з клавіатури.

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email = input("enter email ")

if re.match(pattern, email):
    print("Email введений правильно ")
else: 
    print("Email введений не правильно ")     

# 6. Написати програму, яка підраховує кількість:
# слів,
# голосних  
# приголосних 
# знаків пунктуації,
# цифр  
# інших символів. 
# Урахувати, що між словами (а також до і після слів) може бути більше одного пробілу. 
# Приклад виводу програми:
# Загалом символів у рядку тексту – 38, з них:
# Слів – 6
# Голосних літер - 12
# Приголосних літер - 21
# Знаків пунктуації - 2
# Цифр – 0
# Інших символів – 3

text = input("Введіть текст: ")

# Ініціалізуємо лічильники
words_count = 0
golosni_count = 0
prigol_count = 0
punct_count = 0
digits_count = 0
others_count = 0

golosni = "аоуиієяює"
punct = ".,:;!?"

for letter in text:
    
    if letter.isalpha():
        words_count += 1  

        if letter.lower() in golosni:
            golosni_count += 1

        elif letter.lower() in punct:
            punct_count += 1

        else:
            prigol_count += 1

    elif letter.isdigit():
        digits_count += 1

    elif letter.isspace():
        continue  

    else:
        others_count += 1

print("Кількість слів:", words_count)
print("Кількість голосних:", golosni_count)
print("Кількість приголосних:", prigol_count)
print("Кількість знаків пунктуації:", punct_count)
print("Кількість цифр:", digits_count)
print("Кількість інших символів:", others_count)


# 7. Напишіть програму, яка буде друкувати ромбоподібний малюнок 
# на основі введеного рядка (максимальна довжина – 50 символів). 
# Приклад виводу, якщо рядок «testing»:
#        t
#       te
#      tes
#     test
#    testi
#   testin
#  testing
#  esting
#  sting
#  ting
#  ing
#  ng
#  g

text7 = input("Введіть текст: ")

space = " "
if len(text7) <= 50:
    
    #верхня частина

    for n in range(1, len(text7) + 1):

        print(space * (len(text7) - n), end="")
        print(text7[-n:])

    #нижня частина

    for i in range(1, len(text7) + 1):

        print(text7[:(len(text7) - i)])

else:

    print("Рядок дуже довгий")



