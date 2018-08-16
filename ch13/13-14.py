import os


class Shell(object):
    def __init__(self):
        self.cmds = {'ls': 'dir', 'more': 'more', 'cat': 'type', 'cp': 'copy', 'mv': 'ren', 'rm': 'del', 'q': 'Q'}

    def __interpret(self, cmdstr):
        opt = cmdstr.split()
        if opt[0] in self.cmds:
            opt[0] = self.cmds[opt[0]]
        else:
            print("%s: command not found" % opt[0])
        return ' '.join(opt)

    def start(self):
        while True:
            cmdstr = input('unix2dos#')
            cmd = self.__interpret(cmdstr)
            if cmd.upper() == 'Q':
                break
            else:
                os.system(cmd)


if __name__ == '__main__':
    u2d = Shell()
    u2d.start()
