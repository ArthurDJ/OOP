import abc


class Customer:
    def __init__(self, name, loyaltyDiscount):
        self.name = name
        self.loyaltyDiscount = loyaltyDiscount


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.itemOrdered = []
        self.cost = 0

    def addToOrder(self, Item):
        self.itemOrdered.append(Item)
        self.cost += Item.price

    def summariseOrder(self):
        print("Customer: " + self.customer.name)
        print("Total items ordered number:" + str(len(self.itemOrdered)))
        for i in self.itemOrdered:
            i.displayDetails()
        if self.customer.loyaltyDiscount:
            saving = 0
            for i in self.itemOrdered:
                saving += i.discount
            self.cost -= saving
            print("Today you saved £%.2f" % saving, end='\n')
        print("Total cost: £%.2f" % self.cost, end='\n')


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def displayDetails(self):
        print("Name is %s, price if %.2f" % (self.name, self.price), end='\n')


class Drink(Item):
    def __init__(self, name, price, size):
        super(Drink, self).__init__(name, price)
        self.size = size
        self.discount = 0.1

    def displayDetails(self):
        print("Name is %s, price if %.2f,%s" % (self.name, self.price, self.size), end='\n')


class Tea(Drink):
    def __init__(self, name, price, size, flavour):
        super(Tea, self).__init__(name, price, size)
        self.flavour = flavour

    def displayDetails(self):
        print("Name is %s, price is %.2f,%s,%s" % (self.name, self.price, self.size, self.flavour), end='\n')


class MineralWater(Drink):
    def __init__(self, name, price, size, isCarbonated):
        super().__init__(name, price, size)
        self.isCarbonated = isCarbonated

    def displayDetails(self) -> object:
        print("Name is %s, price is %.2f,%s" % (self.name, self.price, self.size), end='\n')
        if self.isCarbonated:
            print('Sparking water')
        else:
            print('Still water')


class Cake(Item):
    def __init__(self, name, price, sliceSize, type, hasNuts):
        super(Cake, self).__init__(name, price)
        self.sliceSize = sliceSize
        self.type = type
        self.hasNuts = hasNuts
        self.discount = 0

    def displayDetails(self):
        print("Name is %s, price is %.2f,%s,%s" % (self.name, self.price, self.sliceSize, self.type), end='\n')
        if self.hasNuts:
            print('Warning: contains nuts!')
        else:
            print('Free of nuts')


class Sandwich(Item):
    def __init__(self, name, price, breadType, filling):
        super(Sandwich, self).__init__(name, price)
        self.breadType = breadType
        self.filling = filling
        self.discount = 0.2

    def displayDetails(self):
        print("Name is %s, price is %.2f,%s,%s filling" % (self.name, self.price, self.breadType, self.filling),
              end='\n')


def main():
    # Create two customers ...
    cust1 = Customer('Harry Palmer', False)
    cust2 = Customer('Bill Preston', True)  # A loyal regular customer

    # Order some items ...
    order1 = Order(cust1)
    order1.addToOrder(Tea('Black tea', 2.00, 'large', 'Earl Gray'))
    order1.addToOrder(Sandwich('Club special', 4.50, 'brown', 'chicken'))

    order2 = Order(cust2)
    order2.addToOrder(MineralWater('Evian', 1.50, 'small', False))
    order2.addToOrder(Sandwich('Simple sandwich', 1.50, 'white', 'cheese'))
    order2.addToOrder(Cake('Chocolate dream', 2.30, 'medium', 'chocolate', True))

    # Summarise our orders ...
    order1.summariseOrder()
    print()
    order2.summariseOrder()
    print()


if __name__ == "__main__":
    main()
