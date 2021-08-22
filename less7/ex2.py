#Реализовать проект расчета суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#К типам одежды в этом проекте относятся пальто и костюм.
#У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
#Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
#Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_square_c(self):
        return self.width / 6.5 + 0.5
    def get_square_j(self):
        return self.height * 2 + 0.3
    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани - {int(self.width / 6.5 + 0.5) + int(self.height * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, width):
        self.width = width
        self.square_c = round(self.width / 6.5 + 0.5)
    def __str__(self):
        return f'Площадь на пальто {self.square_c}'

class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        self.square_j = round(self.height * 2 + 0.3)
    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(8)
suit = Suit(1)
clothes = Clothes(8, 1)
print(coat)
print(suit)
print(clothes.get_sq_full)