"""Дано вещественное число — цена 1 кг конфет.
 Вывести стоимость 1.2, 1.4, …, 2 кг конфет."""

A = int(input("Введите стоимость 1 кг конфет: "))
import numpy as np

for i in np.linspace(1.2, 2, 5):
    B = A*i
    print (f"Стоимость {i} кг конфет {B} руб.")
    

