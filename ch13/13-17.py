# -*- coding:utf-8 -*-
# 因为__new__实例化的是不可变对象，所以不需要实现update方法
class MoneyFmt(float):
    def __new__(cls, value=0.0):
        return super(MoneyFmt, cls).__new__(cls, value)

    def __init__(self, value=0.0, flag='-'):
        self.flag = flag
        self.mvalue = value

    def dollarize(self):
        val = round(self.mvalue, 2)
        strvalue = str(val)
        pos = strvalue.find('.')
        while (pos - 3) > 0:
            strvalue = strvalue[:pos - 3] + ',' + strvalue[pos - 3:]
            pos -= 3
        if strvalue.startswith('-'):
            return self.flag + '$' + strvalue[1:]
        else:
            return '$' + strvalue

    def __nonzero__(self):
        if (self.mvalue == 0):
            return False
        else:
            return True

    def __str__(self):
        return self.dollarize()


mf = MoneyFmt(100)
print mf
