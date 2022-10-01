#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import numbers


N = int(input('Введите число: '))
num = []
number = []
for j in range(-N, N+1):
    num.append(j)
f = open('file.txt', 'r+')  
n1 = int(f.read(1))  
n2 = int(f.read(2))
mult = num[n1] * num[n2]
print(f'массив -> {num}. произведение элементов на позициях {n1} и {n2} -> {mult}')
for i in range(len(num)):
    number.append
f.close()    