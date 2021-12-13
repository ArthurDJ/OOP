# A simple 2 class implementation for an online shopping
# application
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
           Returns True is removed, False if not present"""
        if item in self.basket:
            self.cost -= item.price
            self.basket.remove(item)
            return True
        else:
            print('Not in the basket')
            return False

    def removeItemByName(self, name):
        """Removes an item from the basket
           Returns True is removed, False if not present"""
        for i in self.basket:
            if i.name == name:
                self.cost -= i.price
                self.basket.remove(i)
                return True
        # If we get here, the named item was not in the basket
        return False

    def showCost(self):
        """Returns the total cost of the basket"""
        print(f'Total cost is £{self.cost:.2f}')
        return self.cost

    def discountBasket(self, rate):
        """Make a discount of rate %
           Returns True is rate is between 10 ro 50% inclusive, False otherwise"""
        if 10.0 <= rate <= 50.0:
            for i in self.basket:
                disc = i.price * (rate / 100)
                i.price = i.price - disc
                self.cost -= disc
            return True
        else:
            print('Invalid rate')
            return False

    def removeAll(self):
        self.basket.clear()
        self.cost = 0.0


class Item:
    """Represents something we can buy in an online shop"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def changeName(self, newName):
        self.name = newName


class TestShoppingApplication(unittest.TestCase):

    def setUp(self):
        self.c1 = Customer('bob', 'bob@acme.com')
        self.c2 = Customer('alice', 'alice@acme.com')
        self.c3 = Customer('jimmy', 'jimmy@acme.com')
        self.i1 = Item('small table', 50)
        self.i2 = Item('table lamp', 30)
        self.i3 = Item('rug', 100)

    def tearDown(self):
        # print("del")
        # del self
        pass

    def test_1(self):
        self.c1.buyItem(self.i1)
        self.c1.buyItem(self.i2)
        self.c2.buyItem(self.i1)
        self.c2.buyItem(self.i3)

        # Checks that the value of the c1 basket is £80.
        self.assertEqual(80, self.c1.showCost(), "Checks that the value of the c1 basket is £80")
        # Checks that the value of the c2 basket is £150.
        self.assertEqual(150, self.c2.showCost(), "Checks that the value of the c2 basket is £150.")
        # Checks that the value of the c3 basket is £0.
        self.assertEqual(0, self.c3.showCost(), "Checks that the value of the c3 basket is £0.")
        # Removes i1 from the c1 basket correctly.
        self.assertTrue(self.c1.removeItem(self.i1), "Removes i1 from the c1 basket correctly.")
        # Checks that i3 cannot be removed from the c1 basket.
        self.assertFalse(self.c1.removeItem(self.i3), "Checks that i3 cannot be removed from the c1 basket.")
        # Removes a table lamp by name from the c1 basket.
        self.assertTrue(self.c1.removeItemByName('table lamp'), "Removes a table lamp by name from the c1 basket.")
        # Removes a small table by name from the c2 basket.
        self.assertTrue(self.c2.removeItemByName('small table'), "Removes a small table by name from the c2 basket.")
        # Checks that the value if the c1 basket is now £0.
        self.assertEqual(0, self.c1.showCost(), "Checks that the value if the c1 basket is now £0.")
        # Checks that the value of the c2 basket is now £100.
        self.assertEqual(100, self.c2.showCost(), "Checks that the value of the c2 basket is now £100.")

    def test_2(self):
        self.c1.buyItem(self.i1)
        self.c1.buyItem(self.i2)
        self.c2.buyItem(self.i1)
        self.c2.buyItem(self.i3)
        self.c3.buyItem(self.i3)

        # Correctly changes the i3 name to ‘red rug’.
        self.i3.changeName('red rug')
        # Checks that the value of the c1 basket is £80.
        self.assertEqual(80, self.c1.showCost(), "Checks that the value of the c1 basket is £80")
        # Checks that the value of the c2 basket is £150.
        self.assertEqual(150, self.c2.showCost(), "Checks that the value of the c2 basket is £150.")
        # Checks that the value of the c3 basket is £100.
        self.assertEqual(100, self.c3.showCost(), "Checks that the value of the c3 basket is £100.")
        # Correctly applies a discount of 10% to the c1 basket (making it worth £72).
        self.assertTrue(self.c1.discountBasket(10), "Correctly applies a discount of 10% to the c1 basket.")
        # Checks that the value of the c1 basket is now £72.
        self.assertEqual(72, self.c1.showCost(), "Checks that the value of the c1 basket is now £72.")
        # Tries to apply a discount of 60% to the c2 basket, but does not succeed.
        self.assertFalse(self.c2.discountBasket(60),
                         "Tries to apply a discount of 60% to the c2 basket, but does not succeed.")
        # Checks that the value of the c2 basket remains as £150.
        self.assertEqual(150, self.c2.showCost(), "Checks that the value of the c2 basket remains as £150.")


if __name__ == '__main__':
    unittest.main()
