""" Дано вещественное число — цена 1 кг конфет.
 Вывести стоимость 0.1, 0.2, …, 1 кг конфет."""

A = int(input("Введите стоимость 1 кг конфет: "))
import numpy as np

for i in np.arange(0.1, 1.1, 0.1):
    B = A*i
    print (f"Стоимость {i} грамм конфет {B} руб.")
    

