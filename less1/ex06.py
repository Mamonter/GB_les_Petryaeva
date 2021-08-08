one_day = int(input("Введите результаты пробежки первого дня>>>"))
all_rez = int(input("Введите желаемый результат>>> "))
days = 1
km = one_day
while km < all_rez:
        one_day = one_day + 0.1 * one_day
        days += 1
        km = km + one_day
print(f"Спортсмен достиг результата на %.d день" % days)
