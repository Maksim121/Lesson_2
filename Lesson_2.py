#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print ('Task N_1')
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
print ('Task N_2')
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
print ('Task N_3')
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
print ('Task N_4')
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
print ('Task N_5')
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


'''
Задача 7
Найти произведение цифр числа.
'''

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''


'''
Задача 10
Найти количество цифр 5 в числе
'''