user = input('Введите выражение: ')

def umnoschenie(a, b):
    return a * b

def summa(a, b):
    return a + b

def rasnost(a, b):
    return a - b 

def delenie(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def separate(string: str, separator):
    result = string.split(separator)
    return [int(x) for x in result] 

if "+" in user:
    numbers = separate(user, "+")
    print(summa(numbers[0], numbers[1]))

elif "-" in user:
    numbers = separate(user, "-")
    print(rasnost(numbers[0], numbers[1]))

elif "*" in user:
    numbers = separate(user, "*")
    print(umnoschenie(numbers[0], numbers[1]))

elif "/" in user:
    numbers = separate(user, "/")
    print(delenie(numbers[0], numbers[1]))

else:
    print('Неправильный ввод')