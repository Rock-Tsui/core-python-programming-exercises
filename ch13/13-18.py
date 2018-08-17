import os
import pickle
from datetime import datetime


class UserList(list):
    def __init__(self):
        super(UserList, self).__init__([])
        self.dbfile = 'db'
        self.loginflag = {}
        self.valid = 365
        if os.path.exists(self.dbfile):
            with open(self.dbfile) as f:
                self.extend(pickle.load(f))

    def __str__(self):
        return '%s' % [item for item in self]

    def savedb(self):
        with open(self.dbfile, 'wb') as f:
            pickle.dump(self, f)

    def newuser(self, name, pwd):
        for usr in self:
            if usr[0] == name:
                print '%s already exist, please login.' % name
                return
        self.append([name, pwd, datetime.now()])

    def login(self, name, pwd):
        for i in xrange(len(self)):
            if (self[i][0] == name) and (self[i][1] == pwd):
                if self.loginflag.get(name, False):
                    print 'You have already login.'
                    break
                self.loginflag[name] = True
                self.__operator()
                break
            elif (self[i][0] == name) and (self[i][1] != pwd):
                print "%s's password is not correct." % name
            elif (i + 1) == len(self):
                print '%s is not exist in database, please add first.' % name

    def deluser(self, name):
        if not self.loginflag.get(name, False):
            print '%s, please login first!' % name
            return
        for i in xrange(len(self)):
            if self[i][0] == name:
                self.pop(i)

    def updatepwd(self, name, pwd):
        if not self.loginflag.get(name, False):
            print '%s, please login first!' % name
            return
        for i in xrange(len(self)):
            if self[i][0] == name:
                if self[i][1] == pwd:
                    if (datetime.now().date() - self[i][2].date()).days <= self.valid:
                        print 'Your pwd is not expired, pls change one'
                else:
                    self[i][1] = pwd
                    self[i][2] = datetime.now()

    def __operator(self):
        print 'Help yourself!'


if __name__ == '__main__':
    user1 = UserList()
    #print user1
    #user1.newuser('root1', 'r1')
    #user1.newuser('root2', 'r2')
    user1.login('root1', 'r1')
    user1.login('root1', 'r1')
    user1.updatepwd('root2', 'r2')
    #user1.deluser('root2')
    print user1
    #user1.login('root1', 'r1')
    #user1.savedb()
