class MoneyFmt(object):
    def __init__(self, val):
        self.val = val

    def update(self, val):
        self.val = val

    def __nonzero__(self):
        return True if self.val else False

    def __repr__(self):
        return repr(self.val)

    def __str__(self):
        if self.val >= 0:
            ret = '{0}{1:,.2f}'.format('$', self.val)
        else:
            ret = '-' + '{0}{1:,.2f}'.format('$', abs(self.val))
        return ret


mf = MoneyFmt(-1234.099)
print(mf)
