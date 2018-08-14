class PerlArray(object):
    def __init__(self, pa=[]):
        self.pa = pa

    def shift(self):
        if len(self.pa) > 0:
            return self.pa.pop(0)
        else:
            return 'PerlArray is empty!'

    def unshift(self, elm):
        self.pa.insert(0, elm)

    def push(self, elm):
        self.pa.append(elm)

    def pop(self):
        if len(self.pa) > 0:
            self.pa.pop()
        else:
            print('PerlArray is empty!')

    def __str__(self):
        return str(self.pa)


q = PerlArray()
print(q.shift())
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.shift())
print(q.pop())
print(q)
q.unshift(5)
print(q)
