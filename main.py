# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
i = 1
while i < 6:
    print(i, '0000000000000000')
    i = i + 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
a = input('1st number')
b = input('2nd number')
c = input('3rd number')
d = input('4th number')
e = input('5th number')
f = input('6th number')
g = input('7th number')
h = input('8th number')
i = input('9th number')
j = input('10th number')
sum = 0
if (int(a)) == 5:
    sum = sum + 1
if (int(b)) == 5:
    sum = sum + 1
if (int(c)) == 5:
    sum = sum + 1
if (int(d)) == 5:
    sum = sum + 1
if (int(e)) == 5:
    sum = sum + 1
if (int(f)) == 5:
    sum = sum + 1
if (int(g)) == 5:
    sum = sum + 1
if (int(h)) == 5:
    sum = sum + 1
if (int(i)) == 5:
    sum = sum + 1
if (int(j)) == 5:
    sum = sum + 1
print(sum)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1, 101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
p = 1
for i in range(2, 11, ):
    p = p * i
print(p)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 7856

# print(integer_number%10,integer_number//10)

while integer_number > 0:
    print(integer_number // 1000)
    integer_number = integer_number % 1000
    print(integer_number // 100)
    integer_number = integer_number % 100
    print(integer_number // 10)
    integer_number = integer_number % 10
    print(integer_number)
    integer_number = integer_number // 10

'''
Задача 6
Найти сумму цифр числа.
'''
a = 8649
sum = 0
while a > 10:
    sum += a // 1000  # 8
    a = a % 1000  # 649
    sum += a // 100  # 8+6
    a = a % 100  # 49
    sum += a // 10  # 14+4
    a = a % 10  # 9
    sum += a  # 18+9
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
r = 4526
p = 1
while r > 10:
    p = r // 1000  # 4
    r = r % 1000  # 526
    p = r // 100 * p  # 5*4
    r = r % 100  # 26
    p = r // 10 * p  # 2*20
    r = r % 10  # 6
    p = p * r  # 40*6

print(p)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else:
    print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
for i in range(9, -1, -1):
    a = 4765300002133
    while a > 0:
        b = a % 10
        if b == i:
            print(i)
            break
        else:
            a = a // 10
    if b == i: break

'''
Задача 10
Найти количество цифр 5 в числе
'''
int_num = 213556413
sum = 0
while int_num > 0:
    if int_num % 10 == 5:
        sum = sum + 1
    int_num = int_num // 10
print(sum)
