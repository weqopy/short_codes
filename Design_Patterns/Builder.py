class Base:
    name = ""
    price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Burger(Base):
    type = "burger"


class Snack(Base):
    type = "snack"


class Beverage(Base):
    type = "beverage"


class CheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class SpicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


class ChipsSnack(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class ChickenWingsSnack(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class CokeBeverage(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class MilkBeverage(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class Order:
    burger = ""
    snack = ""
    beverage = ""

    def __init__(self, orderbuilder):
        self.burger = orderbuilder.build_burger
        self.snack = orderbuilder.build_snack
        self.beverage = orderbuilder.build_beverage

    def show(self):
        print("Burger: {}".format(self.burger.get_name()))
        print("Snack: {}".format(self.snack.get_name()))
        print("Beverage: {}".format(self.beverage.get_name()))


class OrderBuilder:
    build_burger = ""
    build_snack = ""
    build_beverage = ""

    def add_burger(self, xburger):
        self.build_burger = xburger

    def add_snack(self, xsnack):
        self.build_snack = xsnack

    def add_beverage(self, xbeverage):
        self.build_beverage = xbeverage

    def build(self):
        return Order(self)


if __name__ == "__main__":
    order_builder = OrderBuilder()
    order_builder.add_burger(SpicyChickenBurger())
    order_builder.add_snack(ChipsSnack())
    order_builder.add_beverage(MilkBeverage())
    order_1 = order_builder.build()
    order_1.show()
