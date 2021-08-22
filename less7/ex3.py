#Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
#В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
#В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
#Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, x):
        if x and isinstance(x, int):
            self.count = x
        else:
            self.count = 0
            print(f"Cell count ERROR {str(x)}")
    def __add__(self, cell):
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count + cell.count))
    def __sub__(self, cell):
        if cell and isinstance(cell, Cell):
            if self.count > cell.count:
                return Cell(int(self.count - cell.count))
            else:
                print(f"клетка {self.count} не больше {cell.count}")
    def __mul__(self, cell):
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count * cell.count))
    def __truediv__(self, cell):
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count // cell.count))
    def __str__(self):
        return f"клетка размером {self.count} ячеек"
    def make_order(self, col):
        tmp_str = ""
        if col and isinstance(col, int):
            row = self.count // col
            row_end = self.count % col
            while row:
                tmp_str += ("*" * col) + "\n"
                row -= 1
            tmp_str += ("*" * row_end)
        else:
            print(f"Cell make_order ERROR {str(col)}")
        return tmp_str

cell_1 = Cell(23)
cell_2 = Cell(13)
cell_3 = Cell(17)
cell_4 = Cell(55)
cell_5 = Cell(41)

print(f"Ситуация у нас такая:\n{cell_1}\n{cell_2}\n{cell_3}\n{cell_4}\n{cell_5}")
print()
print(f"клетка 1 захватила клетку 2, результат: {cell_1 + cell_2}")
print(f"клетка 3 напала на клетку 4, вышла ошибка : {cell_3 - cell_4}")
print(f"клетка 4 отжала клетку 5, остаток: {cell_4 - cell_5}")
print(f"клетки 2 и 3 объединились,результат: {cell_2 * cell_3}")
print(f"клетки 4 и 1 подрались, получилась : {cell_4 / cell_1}")
print()
print(f"обьединение клеток 2 и 3 :\n{(cell_2 * cell_3).make_order(50)}")
print(f"то что осталось от клеток 4 и 1 :\n{(cell_4 / cell_1).make_order(5)}")
print(f"сильная и независимая клетка 5 :\n{cell_5.make_order(15)}")