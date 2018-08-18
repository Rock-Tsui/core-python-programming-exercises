#!/usr/bin/env python


class Time60(object):
    def __init__(self, hr=0, min=0):
        if isinstance(hr, str):
            ret = hr.split(':')
            self.hr = int(ret[0])
            self.min = int(ret[1])
        else:
            self.hr = hr
            self.min = min

    def __str__(self):
        return '%s:%s' % (str(self.hr).zfill(2), str(self.min).zfill(2))

    def __repr__(self):
        return repr('%02d:%02d' % (self.hr, self.min))

    def __add__(self, other):
        rhr = self.hr + other.hr + (self.min + self.min) // 60
        rmin = (self.min + other.min) % 60
        return self.__class__(rhr, rmin)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

    def __sub__(self, other):
        if self.min < other.min:
            self.hr -= 1
            self.min += 60
        return self.__class__(self.hr - other.hr, self.min - other.min)

    def __int__(self):
        return self.hr * 60 + self.min


if __name__ == '__main__':
    # wed = Time60(12, 5)
    # wed = Time60(*(10, 30))
    # wed = Time60(**{'hr': 10, 'min': 30})
    # wed = Time60(hr=10, min=30)
    # wed = Time60("10:30")
    thu = Time60(10, 30)
    fri = Time60(8, 45)
    print(thu - fri)
    print(int(thu))
