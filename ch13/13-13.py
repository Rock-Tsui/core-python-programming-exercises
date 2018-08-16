class stock(object):
    def __init__(self):
        self.name = ''
        self.symbol = ''
        self.date = ''
        self.price = ''
        self.number = 0


class StockPortfolio(object):
    def __init__(self):
        self.stockdb = {}

    def purchase(self, st):
        self.stockdb.setdefault(st.symbol, st)

    def sold(self, symb):
        self.stockdb.pop(symb, None)

    def getYTD(self, symb, cprice, cdate):
        pass


sp = StockPortfolio()
