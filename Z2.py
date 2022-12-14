# Задание 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Единственный класс этого проекта — одежда (класс Clothes).
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
# для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать
# абстрактный класс для единственного класса проекта,
# проверить на практике работу декоратора @property
# Пример:
# Расход ткани на пальто = 1.27
# Расход ткани на костюм = 20.30
# Общий расход ткани = 21.57
# Два класса: абстрактный и Clothes

from abc import ABC, abstractmethod

class Abstract:

    @abstractmethod
    def get_coat_need(self):
        pass

    @abstractmethod
    def get_suit_need(self):
        pass

    def get_total_need(self):
        pass

class Clothes(Abstract):

    def __init__(self, v, h):
        self.v = int(v)
        self.h = int(h)
        self.coat_need = self.v / 6.5 + 0.5
        self.suit_need = 2 * self.h + 0.3

    def __str__(self):
        return f'\nРасход ткани на пальто: {self.coat_need} метров\nРасход ткани на костюм: {self.suit_need} метров\nОбщая потребность в ткани: {self.coat_need + self.suit_need} метров\n'

costume = Clothes(55, 20)
print(costume)