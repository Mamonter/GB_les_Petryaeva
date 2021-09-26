#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summa():
    try:
        with open("file_5.txt", "w+") as numbers:
            line = input('Введите целые числа через пробел \n')
            numbers.writelines(line)
            my_num = line.split()

            print(sum(map(int, my_num)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Проверьте правильность ввода")
summa()