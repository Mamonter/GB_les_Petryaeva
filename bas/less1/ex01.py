
name = input("введите имя  >>>: ")
name2 = input("введите имя  >>>: ")
days = int(input("кол-во дней: >>>"))
night = int(input("кол-во ночей: >>>"))

if days >= night:
    print(f"Однажды в пустыне {name} искал лампу уже {days} дней и {night} ночей")
    print(f"Но {name2} нашел ее первее")
else:
    print(f"Ошибка, {days} должно быть больше или равно {night}")