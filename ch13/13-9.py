class Queue(object):
    def __init__(self, q=[]):
        self.q = q

    def enqueue(self, elm):
        self.q.append(elm)

    def dequeue(self):
        if len(self.q) > 0:
            return self.q.pop(0)
        else:
            return 'Queue is empty!'

    def __str__(self):
        return str(self.q)


q = Queue([0])
print(q.dequeue())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q)
