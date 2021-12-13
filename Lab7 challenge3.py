# A simple 2 class implementation for an online shopping
# application - this time raise and catching exceptions

# Define an exception for ItemNotPresentError ...

# Define an exception for InvalidDiscountRateError ...
import unittest


class Customer:
    """Represents a customer for an online shop"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.basket = []
        self.cost = 0.0

    def buyItem(self, item):
        self.basket.append(item)
        self.cost += item.price

    def removeItem(self, item):
        """Removes an item from the basket
           Raises ItemNotPresentError if not present"""
        try:
            if item not in self.basket:
                raise ItemNotPresentError(item.name, 'not in the basket')
            else:
                self.cost -= item.price
                self.basket.remove(item)
        except ItemNotPresentError:
            pass

    def removeItemByName(self, name):
        """Removes an item from the basket
           Raises ItemNotPresentError if not present"""
        try:
            for i in self.basket:
                if i.name == name:
                    self.cost -= i.price
                    self.basket.remove(i)
                    return
            # If we get here, the named item was not in the basket
            raise ItemNotPresentError(name, 'not in the basket')
        except ItemNotPresentError:
            pass

    def showCost(self):
        """Returns the total cost of the basket"""
        print(f'Total cost is £{self.cost:.2f}')
        return self.cost

    # Rewrite this code so that it raises an InvalidDiscountRateError
    # if the discount rate is not in the stated range ...

    def discountBasket(self, rate):
        """Make a discount of rate %
           Returns True is rate is between 10 ro 50% inclusive, False otherwise"""
        try:
            if 10.0 <= rate <= 50.0:
                for i in self.basket:
                    disc = i.price * (rate / 100)
                    i.price = i.price - disc
                    self.cost -= disc
                return
            raise InvalidDiscountRateError(rate, 'not in 10 ro 50% inclusive')
        except InvalidDiscountRateError:
            pass


class Item:
    """Represents something we can buy in an online shop"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def changeName(self, newName):
        self.name = newName


def main():
    c1 = Customer('bob', 'bob@acme.com')
    c2 = Customer('alice', 'alice@acme.com')
    c3 = Customer('jimmy', 'jimmy@acme.com')
    i1 = Item('small table', 50.0)
    i2 = Item('table lamp', 30.0)
    i3 = Item('rug', 100.0)

    c1.buyItem(i1)
    c1.buyItem(i2)
    c2.buyItem(i1)
    c2.buyItem(i3)
    c3.buyItem(i3)

    # Try to remove items that are not present
    c1.removeItemByName('pot')
    c2.removeItem(i2)
    c3.discountBasket(1000)


class ItemNotPresentError(Exception):
    def __init__(self, name, message):
        print(f'{name} {message}')


class InvalidDiscountRateError(Exception):
    def __init__(self, rate, message):
        print(f'{rate} {message}')


if __name__ == '__main__':
    main()
