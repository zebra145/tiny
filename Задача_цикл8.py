"""Даны два целых числа A и B (A<B). 
Найти произведение всех целых чисел от A до B включительно."""

A=int(input("Введите целое число: "))
B=int(input("Введите целое число: "))

s = 1
for i in range (A, B+1):
    s = i * s
    
print(s)
