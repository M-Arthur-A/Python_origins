'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, name, is_police=False, speed=0, color=None):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} поехала и набрала скорость {self.speed} км/ч!')

    def stop(self):
        if self.speed == 0:
            print(f'{self.name} уже остановилась!')
        else:
            self.speed = 0
            print(f'{self.name} остановилась!')

    def turn(self, direction):
        self.turn = direction
        print(f'{self.name} повернула {self.turn}')

    def show_speed(self):
        pass


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Внимание! Превышена скорость. Снизте до 60 км/ч!')
        pass

    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Внимание! Превышена скорость. Снизте до 40 км/ч!')
        pass

    pass


class PoliceCar(Car):
    def __init__(self, name, speed=None, color=None):
        super().__init__(name, speed, color)
        self.is_police = True


# создаем объекты класса Car
car_town = TownCar('nissan AX250 town', speed=120)
car_sport = SportCar('ferrari')
car_work = WorkCar('toyota camry', speed=60)
car_police = PoliceCar('lada 14')

# тестируем
car_sport.go(240)
car_sport.turn('направо')
print(f'Направление {car_sport.name} -', car_sport.turn)
car_sport.stop()
car_sport.stop()
print(car_sport.name, 'is police? -', car_sport.is_police)
print(car_police.name, 'is police? -', car_police.is_police)
car_work.show_speed()
