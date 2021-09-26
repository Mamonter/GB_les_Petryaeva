# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

list = ['зима', 'весна', 'лето', 'осень']
dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца согласно календарю >> "))
if month ==1 or month == 12 or month == 2:
        print(f"Вы ввели номер {month} - это {dict.get(1)}")
        print(f"значение list = {list[0]}")
elif month == 3 or month == 4 or month ==5:
    print(f"Вы ввели номер {month} - это {dict.get(2)}")
    print(f"значение list = {list[1]}")
elif month == 6 or month == 7 or month == 8:
    print(f"Вы ввели номер {month} - это {dict.get(3)}")
    print(f"значение list = {list[2]}")
elif month == 9 or month == 10 or month == 11:
    print(f"Вы ввели номер {month} - это {dict.get(4)}")
    print(f"значение list = {list[3]}")
else:
        print("вы ввели неверный номер, такого месяца не существует")