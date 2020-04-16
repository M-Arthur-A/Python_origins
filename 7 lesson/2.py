"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name):
        self.name = str(name)

    @abstractmethod
    def consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Smoking(Cloth):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    @property
    def consumption(self):
        return round(self.length / 4 + 0.3, 2)


coat = Coat("Lady's coat", 46)
smoking = Smoking("Man's suit", 50)
print('Расход на женское пальто сосоавляет:', coat.consumption, 'м. ткани.')
print('Расход на мужской костюм стсоавляет:', smoking.consumption, 'м. такни.')
