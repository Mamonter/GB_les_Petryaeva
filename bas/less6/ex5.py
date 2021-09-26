#Создайте экземпляры классов, передайте значения атрибутов.
#Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.


class cl:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return ""
class test(cl):
    def draw(self):
        return f"не совсем понятное задание {self.title}"
test = test("!!??!!")
print(test.draw())