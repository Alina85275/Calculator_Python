class Calc():                                      #Родительский класс

    def __init__(self, x, y):                      #Метод инициализации значений x и y
        self._x = x
        self._y = y


    def set_vale(self, x, y):                      #Метод постановки значений x и y
        self.valid_value(x, y)
        self._x = x
        self._y = y


    def get_value(self):                            #Метод получения значений x и y
        return self._x, self._y

    @classmethod                                    #КлассМетод проверки значений x и y
    def valid_value(cls, x, y):
        if type(x) != int and type(y) != int:
            raise TypeError("not correctly")


    @classmethod                                    #КлассМетод проверки значений x и y с доп параметром, для деления
    def valid_valueDiv(cls, x, y):
        if type(x) != int and x == 0 or type(y) != int and y == 0:
            raise TypeError("not correctly")


    def __str__(self):                               #Метод, который выводит значения x, y в консоль в корректном виде
        return f"{self._x, self._y}"

    
    def result(self):                                #Метод получения результата, который будет переопределен в наседованных классах
        pass

   
class Add(Calc):                             #Наследованный класс от класса Calc
    def __init__(self, x, y):                #переопределение метода инициализации из базового класса
        Calc.__init__(self, x, y)
        self.valid_value(x, y)
        

    def result(self, x, y):                   #переопределение метода resul из базового класса
        super().result()
        print(x + y)
        
    
class Sub(Calc):                               #Наследованный класс от класса Calc
    def __init__(self, x, y):                  #переопределение метода инициализации из базового класса
        Calc.__init__(self, x, y)
        self.valid_value(x, y)
        

    def result(self, x, y):                    #переопределение метода resul из базового класса
        super().result()
        print(x - y)


class Multi(Calc):                             #Наследованный класс от класса Calc 
    def __init__(self, x, y):                  #переопределение метода инициализации из базового класса
        Calc.__init__(self, x, y)
        self.valid_value(x, y)
        

    def result(self, x, y):                    #переопределение метода resul из базового класса
        super().result()
        print(x * y)


class Div(Calc):                               #Наследованный класс от класса Calc        


    def __init__(self, x, y):                  #переопределение метода инициализации из базового класса
        Calc.__init__(self, x, y)
        self.valid_valueDiv(x, y)


    def result(self, x, y):                    #переопределение метода resul из базового класса
        super().result()
        print(x / y)