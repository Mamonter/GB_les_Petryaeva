viruchka = float(input("Введите пожалуйста выручку фирмы >>>"))
izder = float(input("Теперь введи издержки фирмы >>> "))
if viruchka > izder:
    print(f"Ваша фирма работает с прибылью! Рентабельность выручки {viruchka / izder:.2f}")
    person = int(input("Требуется ввести количество сотрудников фирмы >>> "))
    print(f"Прибыль на одного сторудника {viruchka / person:.2f}")
elif viruchka == izder:
    print("Данная фирма работает в 0")
else:
    print("Фирма в убытке")