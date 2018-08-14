class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return '(%s, %s)' % (self.name, self.price)


class Cart(object):
    def __init__(self, name):
        self.name = name
        self.itemsdict = {}

    def isempty(self):
        if len(self.itemsdict) == 0:
            return True
        else:
            return False

    def additem(self, item, count=1):
        if item not in self.itemsdict:
            self.itemsdict[item] = count
        else:
            self.itemsdict[item] += count

    def delitem(self, item, count=1):
        if item in self.itemsdict and self.itemsdict[item] > count:
            self.itemsdict[item] -= count
        elif item in self.itemsdict and self.itemsdict[item] == count:
            self.itemsdict.pop(item)
        else:
            print '%s is not in %s!' % (item, self.name)

    def showitem(self):
        for item in self.itemsdict:
            print '{0} {1}, {2}'.format(self.name, item, self.itemsdict[item])


class User(object):
    def __init__(self, name):
        self.name = name
        self.cartlist = []

    def addcart(self, cart):
        if cart not in self.cartlist:
            self.cartlist.append(cart)
        else:
            print "%s already have %s" % (self.name, cart.name)

    def delcart(self, cart):
        if cart in self.cartlist:
            self.cartlist.remove(cart)
        else:
            print "%s didn't have %s" % (self.name, cart)

    def showcart(self):
        for cart in self.cartlist:
            print '%s has %s' % (self.name, cart.name)


apple = Item('apple', 8.5)
pear = Item('pear', 5)
ct = Cart('cart1')
ct.additem(apple, 2)
ct.additem(pear, 2)
ct.delitem(apple, 1)
ct.showitem()
ur = User('Jim')
ur.addcart(ct)
ur.showcart()
ur.addcart(ct)
