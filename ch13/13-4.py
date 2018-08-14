import time
import pickle


class UserData(object):
    def __init__(self):
        self.db = {}

    def __del__(self):
        with open('db', 'wb') as f:
            pickle.dump(self.db, f)

    def newuser(self):
        prompt = 'login desired: '
        while 1:
            name = input(prompt)
            if name in self.db:
                prompt = 'name taken, try another: '
                continue
            else:
                break
        pwd = input('passwd: ')
        self.db[name] = {'pwd': pwd, 'date': time.ctime()}

    def olduser(self):
        name = input('login: ')
        pwd = input('passwd: ')
        passwd = self.db[name]['pwd']
        if passwd == pwd:
            pass
        else:
            print('login incorrect')
            return

        print('welcome back', name)
        print('The last login time is', self.db[name]['date'])


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    # loop until user quits
    done = 0
    usrd = UserData()
    while not done:

        # loop until user choses valid option
        chosen = 0
        while not chosen:

            # if user hits RETURN/Enter, ^C, or ^D (EOF),
            # pretend they typed 'q' to quit normally
            try:
                choice = input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)

            # validate option chosen
            if choice not in 'neq':
                print('invalid menu option, try again')
            else:
                chosen = 1

        # take appropriate action
        if choice == 'q':
            done = 1
        if choice == 'n':
            usrd.newuser()
        if choice == 'e':
            usrd.olduser()


# run showmenu() as the application
if __name__ == '__main__':
    showmenu()
