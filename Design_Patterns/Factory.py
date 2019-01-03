import abc

## Simple Factory
class Mercedes:
    def __repr__(self):
        return "Mercedes-Benz"


class BMW:
    def __repr__(self):
        return "BMW"


class SimpleCarFactory:
    @staticmethod
    def product_car(name):
        if name == "mb":
            car = Mercedes()
        elif name == "bmw":
            car = BMW()
        else:
            return "wrong name"
        return car


def test_SimpleCarFactory():
    c1 = SimpleCarFactory.product_car("mb")
    c2 = SimpleCarFactory.product_car("bmw")
    print(c1, c2)


## Factory Method


class AbstractFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass


class MercedesFactory(AbstractFactory):
    def product_car(self):
        return Mercedes()


class BMWFactory(AbstractFactory):
    def product_car(self):
        return BMW()


class Audi:
    def __repr__(self):
        return "Audi"


class AudiFactory(AbstractFactory):
    def product_car(self):
        return Audi()


def test_FactoryMethod():
    c1 = MercedesFactory().product_car()
    c2 = BMWFactory().product_car()
    c3 = AudiFactory().product_car()
    print(c1, c2, c3)


## AbstractFactory
class Mercedes_C63:
    def __repr__(self):
        return "Mercedes-Benz: C63"


class BMW_M3:
    def __repr__(self):
        return "BMW: M3"


class Mercedes_G63:
    def __repr__(self):
        return "Mercedes-Benz: G63"


class BMW_X5:
    def __repr__(self):
        return "BMW: X5"


class New_AbstractFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass

    @abc.abstractmethod
    def product_suv(self):
        pass


class New_MercedesFactory(AbstractFactory):
    def product_car(self):
        return Mercedes_C63()

    def product_suv(self):
        return Mercedes_G63()


class New_BMWFactory(AbstractFactory):
    def product_car(self):
        return BMW_M3()

    def product_suv(self):
        return BMW_X5()


def test_AbstractFactory():
    c1 = New_MercedesFactory().product_car()
    s1 = New_MercedesFactory().product_suv()
    print(c1, s1)
    s2 = New_BMWFactory().product_suv()
    c2 = New_BMWFactory().product_car()
    print(c2, s2)


if __name__ == "__main__":
    test_list = [test_SimpleCarFactory, test_FactoryMethod, test_AbstractFactory]
    for func in test_list:
        print("*" * 13)
        func()
