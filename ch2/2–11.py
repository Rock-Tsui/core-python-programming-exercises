def numbers_sum():
    print sum(input("Input number:") for i in range(5))


def numbers_ave():
    print sum(input("Input number:") for i in xrange(5)) / 5


if __name__ == '__main__':
    usage = '''
    (1) Sum of five numbers
    (2) Average of five numbers
    (X) Quit
    Please select:
    '''
    while True:
        opt = raw_input(usage)
        if opt == '1':
            numbers_sum()
        elif opt == '2':
            numbers_ave()
        elif opt == 'X':
            break
