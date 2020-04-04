#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print ('Task N_1: вывести на экран циклом пять строк из нулей и пронумеровать их')
i1=1
while i1<=5:
    print (i1,'0000000000')
    i1=i1+1
print('End of Task N_1')
print('_____________')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print ('Task N_2: найти количество введённых пользователем цифр 5')
i2=1
n5=0
while i2<=10:
    a2=input ('Введите цифру от 0 до 9: ')
    a2=int(a2)
    i2 = i2 +1
    if a2==5:
        n5=n5+1
print('Пользователь ввёл ', n5, ' раз(а) цифру 5')
print('End of Task N_2')
print('_____________')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print ('Task N_3: найти сумму ряда чисел от 1 до 100')
sum3 = 0

for i3 in range(1,101):
     sum3+=i3
print('Сумма ряда чисел от 1 до 100 = ', sum3)

print('End of Task N_3')
print('_____________')
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print ('Task N_4: найти произведение ряда чисел от 1 до 10')
sum4 = 1

for i4 in range(1,11):
     sum4=sum4*i4
print('Произведение ряда чисел от 1 до 10 = ', sum4)

print('End of Task N_4')
print('_____________')
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print ('Task N_5: вывести цифры числа на каждой строчке')
integer_number5 = input('Введите целое число: ')
integer_number5=int(integer_number5)

#print(integer_number%10,integer_number//10)

while integer_number5>0:
     print(integer_number5%10)
     integer_number5 = integer_number5//10

print('End of Task N_5')
print('_____________')
'''
Задача 6
Найти сумму цифр числа.
'''
print ('Task N_6: найти сумму цифр числа')
integer_number6 = input('Введите целое число: ')
integer_number6=int(integer_number6)

#print(integer_number%10,integer_number//10)
i6=0
while integer_number6>0:
     print(integer_number6%10)
     k6=integer_number6%10
     i6 = i6 + k6
     integer_number6 = integer_number6//10
print('Сумма цифр введённого числа= ',i6)
print('End of Task N_6')
print('_____________')

'''
Задача 7
Найти произведение цифр числа.
'''
print ('Task N_7: найти произведение цифр числа')
integer_number7 = input('Введите целое число: ')
integer_number7=int(integer_number7)

#print(integer_number%10,integer_number//10)
i7=1
while integer_number7>0:
     print(integer_number7%10)
     k7=integer_number7%10
     i7 = i7 * k7
     integer_number7 = integer_number7//10
print('Произведение цифр введённого числа= ',i7)
print('End of Task N_7')
print('_____________')
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print ('Task N_8: есть ли среди цифр числа цифра 5')
integer_number8 = input('Введите целое число: ')
integer_number8=int(integer_number8)
while integer_number8>0:
    if integer_number8%10 == 5:
        print('Yes')
        i8='ДА'
        break
    integer_number8 = integer_number8//10
#else: print('No')
else: i8='НЕТ'
print('Есть ли среди цифр введённого числа цифра 5? ', i8)
print('End of Task N_8')
print('_____________')
'''
Задача 9
Найти максимальную цифру в числе
'''
print ('Task N_9: найти максимальную цифру в числе')
integer_number9 = input('Введите целое число: ')
integer_number9=int(integer_number9)

#print(integer_number%10,integer_number//10)
i9=0
while integer_number9>0:
     print(integer_number9%10)
     k9=integer_number9%10
     integer_number9 = integer_number9//10
     if k9>i9:
        i9=k9
print('Максимальная цифра в ведённом числе = ',i9)
print('End of Task N9')
print('_____________')

'''
Задача 10
Найти количество цифр 5 в числе
'''
print ('Task N_10: найти количество цифр 5 в числе')
integer_number10 = input('Введите целое число: ')
integer_number10=int(integer_number10)
k10=0
i10='НЕТ'
while integer_number10>0:
    if integer_number10%10 == 5:
        print('Yes')
        i10='ДА'
        k10=k10+1
#        break
    integer_number10 = integer_number10//10
#else: print('No')
#else: i10='НЕТ'
print('Есть ли среди цифр введённого числа цифра 5? ', i10)
print('Сколько раз встречается цифра 5 в введённом числе? ', k10)
print('End of Task N_8')
print('_____________')