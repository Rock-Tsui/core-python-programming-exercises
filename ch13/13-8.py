class Stack(list):
    def __init__(self):
        super(Stack, self).__init__([])

    def __getattr__(self, attr):
        return getattr(self, attr)

    def push(self, elm):
        self.append(elm)

    def isempty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.isempty():
            return self[-1]
        return 'List is empty!'


st = Stack()
print(st.peek())
st.push(1)
st.push(2)
st.push(3)
print(st)
st.pop()
print(st.peek())
print(st)
print(st.isempty())