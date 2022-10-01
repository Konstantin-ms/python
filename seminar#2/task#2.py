#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



from math import radians


n = int(input('Введите число: '))
prod_num = 1
for i in range(1, n+1):
    prod_num *= int(i)
    print(prod_num, end=',')




