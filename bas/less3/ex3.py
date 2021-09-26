#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    znach = [a,b,c]
    znach.sort(reverse=True)
    return znach[0] + znach[1]
res = my_func(int(input("Ввидете число[a] >>")),
                 int(input("Введите число[b] >>")),
                 int(input("Введите число[c] >> ")))
print(f"Возвращаю сумму наибольших аргументов составляет {res}")