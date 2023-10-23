# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть унаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport

# экземпляр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключений


from abc import ABCMeta, abstractmethod, ABC


class Transport(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport, ABC):
    def start_engine(self) -> None:
        print('Двигатель катера запущен')

    def stop_engine(self) -> None:
        print('Двигатель катера заглушен')

    def move(self) -> None:
        print('Движение катера')

    def stop(self) -> None:
        print('stop катера')


class Car(Transport, ABC):
    def start_engine(self) -> None:
        print('Двигатель машины запущен')

    def stop_engine(self) -> None:
        print('Двигатель машины заглушен')

    def move(self) -> None:
        print('Движение машины')

    def stop(self) -> None:
        print('stop машины')


class ElectroScooter(Transport, ABC):
    def start_engine(self):
        print('Двигатель скутера запущен')

    def stop_engine(self) -> None:
        print('Двигатель машины заглушен')

    def move(self) -> None:
        print('Движение машины')

    def stop(self) -> None:
        print('stop машины')


class Person:

    def use_transport(self, obj: ElectroScooter | Boat | Car):
        obj.stop_engine()
        obj.move()
        obj.stop()
        obj.stop_engine()


# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = ElectroScooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
