#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func():
    try:
        a = int(input("Введите первое число >> "))
        b = int(input("Введите второе число >>"))
        result = a / b
    except ZeroDivisionError: #обработка ошибки с делением на ноль!
        return "Внимание! Деление на 0 запрещено"
    return result
print(f'{func()}')