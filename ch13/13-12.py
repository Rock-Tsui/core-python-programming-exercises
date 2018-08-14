class Message(object):
    def __init__(self, msg='', bc=True, fromU='', toU=''):
        self.msg = msg
        self.broadcast = bc
        self.fromU = fromU
        self.toU = toU

    def __str__(self):
        if self.broadcast:
            return 'Message: %s from %s send to everyone' % (self.msg, self.fromU)
        else:
            return 'Message: %s from %s send to %s' % (self.msg, self.fromU, self.toU)


class User(object):
    heared = {}

    def __init__(self, name='', age=0, sex='male'):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return 'name:{0},age:{1},sex:{2}'.format(self.name, self.age, self.sex)

    def talk(self, toU='', msg=''):
        if toU == 'everyone':
            User.heared[toU] = Message(msg, True, self.name)
        elif toU:
            User.heared[toU] = Message(msg, False, self.name, toU)
        else:
            print('receiver cannot be empty!')

    def hear(self):
        if self.name in User.heared:
            print('Receive message from %s: %s' % (User.heared[self.name].fromU, User.heared[self.name].msg))
        if 'everyone' in User.heared:
            print('Receive broadcast message: %s' % User.heared[self.name].msg)

    def talkroom(self, room, toU='', msg=''):
        if toU == 'everyone':
            room.receiver(Message(msg, True, self.name))
        elif toU:
            room.receiver(Message(msg, False, self.name, toU))
        else:
            print('receiver cannot be empty!')

    def hearroom(self, msg):
        print('Room %s' % msg)

    def createroom(self, name, count=3):
        return Room(name, count)


class Room(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.usrlist = []

    def __str__(self):
        return 'name:{0},usrs:{1}'.format(self.name, self.usrlist)

    def adduser(self, usr):
        if usr not in self.usrlist and len(self.usrlist) < self.count:
            self.usrlist.append(usr)

    def receiver(self, msg):
        if msg.broadcast:
            print('Room %s' % msg)
        else:
            for usr in self.usrlist:
                if usr.name == msg.toU:
                    usr.__class__.heared[msg.toU] = msg
                    #usr.hearroom(msg)


usr1 = User('Jim', 23, 'male')
usr2 = User('John', 25, 'male')
usr3 = User('Lucy', 19, 'female')
usr1.talk('John', 'Hello, John!')
usr2.hear()
usr3.hear()
#print(usr3.__class__.heared)
rm1 = Room('Room1', 3)
rm1.adduser(usr1)
rm1.adduser(usr2)
rm1.adduser(usr3)
usr2.talkroom(rm1, 'Lucy', 'Hello, Lucy!')
usr1.hear()
usr3.hear()
