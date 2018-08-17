import os

class CapOpen(object):
    def __init__(self, fn, mode='r', buf=1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return repr(self.file)

    def write(self, line):
        self.file.write(line.upper())

    def writelines(self, lines, nl=False):
        for line in lines:
            if nl:
                line += os.linesep
            self.write(line)

    def __getattr__(self, attr):
        return getattr(self.file, attr)


lt = ['abc', 'def', 'ghi']
copen = CapOpen('input.txt', 'w')
#copen.writelines(lt)
copen.writelines(lt, True)
