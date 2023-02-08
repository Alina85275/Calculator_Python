from Calc.Calc import *
class Menu():                                  #Класс Меню, реализующий меню калькулятора
    def select(self):                          #Метод выбора вида операции и ввода значений
        s = input("Введите число:\n 1. Сложение\n 2. Вычитание\n 3. Умножение\n 4. Деление\n")
        if s == "1":
            a = Add(0, 4)
            print(a.result(int(input("Введите первую цифру")), int(input("Введите вторую цифру"))))
        elif s == "2":
            b = Sub(1, 1)
            print(b.result(int(input("Введите первую цифру")), int(input("Введите вторую цифру")))) 
        elif s == "3":
            c = Multi(1, 1)
            print(c.result(int(input("Введите первую цифру")), int(input("Введите вторую цифру"))))
        elif s == "4":
            d = Div(2, 4)
            print(d.result(int(input("Введите первую цифру")), int(input("Введите вторую цифру"))))
        
b = Menu()  
b.select()


