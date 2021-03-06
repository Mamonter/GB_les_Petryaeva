# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class NumList(Exception):
    def __init__(self, *args):
        self.my_list = []
    def apperlist(self):
        while True:
            el = input('Введите элемент списка, для выхода введите "stop": ')
            if el.upper() == 'stop':
                print(f'Ввод завершен, результат: {self.my_list}')
                break
            try:
                el = float(el)
                self.my_list.append(el)
                print(f'Текущий список: {self.my_list}\n')
            except:
                print(f'Вы ввели не число!\nТекущий список: {self.my_list}\n')

example = NumList([])
example.apperlist()