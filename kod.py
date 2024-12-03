user = input('Введите выражение: ')

def umnoschenie(a, b):# пишем функцию умножения
    return a * b

def summa(a, b):#пишем функцию суммы
    return a + b

def rasnost(a, b):#пишем функцию разности
    return a - b 

def delenie(a, b):#пишем функцию деления
    if b == 0:
        return "Ошибка"
    return a / b

def separate(string: str, separator):
    result = string.split(separator)
    return [float(x) for x in result] 

if "*" in user:
    numbers = separate(user, "*")
    print(umnoschenie(numbers[0], numbers[1]))

elif "+" in user:
    numbers = separate(user, "+")
    print(summa(numbers[0], numbers[1]))

elif "-" in user:
    numbers = separate(user, "-")
    print(rasnost(numbers[0], numbers[1]))

elif "/" in user:
    numbers = separate(user, "/")
    print(delenie(numbers[0], numbers[1]))

else:
    print('Неправильная операция')