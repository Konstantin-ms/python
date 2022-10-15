

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# пример использования list comperehension



from random import randint

lst = [randint(-10, 10) for i in range(4)]
print(lst)

x1 = int(input(lst[0]))
y1 = int(input(lst[1]))
x2 = int(input(lst[2]))
y2 = int(input(lst[3]))
a = ((x2-x1)**2+(y2-y1)**2)**0.5
print(round(a, 2))
