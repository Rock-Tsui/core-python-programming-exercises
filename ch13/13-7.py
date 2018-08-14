import time


class Date(object):
    def __init__(self, date=time.time()):
        self.date = date

    def update(self, date=time.time()):
        self.date = date

    def diplay(self, fmt=''):
        if not fmt:
            return time.ctime(self.date)
        if fmt == 'MDY':  # MM/DD/YY
            fmt = '%m/%d/%y'
        elif fmt == 'MDYY':  # MM/DD/YYYY
            fmt = '%m/%d/%Y'
        elif fmt == 'DMY':  # DD/MM/YY
            fmt = '%d/%m/%y'
        elif fmt == 'DMYY':  # DD/MM/YYYY
            fmt = '%d/%m/%Y'
        elif fmt == 'MODYY':  # Mon DD, YYYY
            fmt = '%a %d, %Y'
        return time.strftime(fmt, time.localtime(self.date))


date = Date()
print date.diplay('DMYY')
