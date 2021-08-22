#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
#Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
#Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return "Запуск отрисовки."

class Pen(Stationery):
    def draw(self):
        return f"Это {self.title}. Ей можно писать"
pen = Pen("Ручка")
print(pen.draw())

class Pencil(Stationery):
    def draw(self):
        return f"Это {self.title}. Им можно чертить и рисовать"
pencil = Pencil("Карандаш")
print(pencil.draw())

class Handle(Stationery):
    def draw(self):
        return f"Это {self.title}. Им можно подчеркивать"
handle = Handle("Маркер")
print(handle.draw())