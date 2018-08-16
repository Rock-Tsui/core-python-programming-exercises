# -*- coding: utf-8 -*-

class Stock(object):
    def __init__(self, name, symbol, date, price, number):
        self.name = name
        self.symbol = symbol
        self.date = date
        self.price = price
        self.number = number

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.name, self.symbol, self.date, self.price, self.number)


class StockPortfolio(object):
    def __init__(self):
        self.stockdb = {}

    def purchase(self, st):
        self.stockdb.setdefault(st.symbol, st)

    def sold(self, symb):
        self.stockdb.pop(symb, None)

    def getYTD(self, symb, cprice, cdate):
        st = self.stockdb.get(symb, None)
        if st:
            capital = st.price * st.number
            totalmoney = cprice * st.number
            profit = totalmoney - capital
            print('%.2f%%' % ((profit / capital) * 100))
        else:
            print('Stock %s does not exist' % symb)

    def showstocks(self):
        [print(st) for st in self.stockdb.values()]


st1 = Stock('中电电机', '603988', '2018/8/16', 16.97, 100)
st2 = Stock('创业软件', '300451', '2018/8/16', 16.57, 100)
sp = StockPortfolio()
sp.purchase(st1)
sp.purchase(st2)
sp.showstocks()
print('\n')
sp.sold('603988')
sp.showstocks()
sp.getYTD('300451', 18, '2018/9/16')
