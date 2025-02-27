class Calculator:
    def __init__(self,num1, num2):
    
        self.num1 = num1
        self.num2 = num2
    
    def summa(self):
        result = self.num1 + self.num2
        print(f"Результат: {result}")
    
    def rasnost(self):
        result = self.num1 - self.num2
        print(f"Результат: {result}")
    
    def umnoschenie(self):
        result = self.num1 * self.num2
        print(f"Результат: {result}")
    
    def delenie(self):
        if self.num2 == 0:
            print("Ошибка: деление на ноль")
        else:
            result = self.num1 / self.num2
            print(f"Результат: {result}")
    def __del__(self):
        print("Класс удален")

numbers = Calculator(20,2)
numbers.delenie()