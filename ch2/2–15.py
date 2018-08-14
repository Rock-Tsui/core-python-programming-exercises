a = input('input number a:')
b = input('input number b:')
c = input('input number c:')

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print a, b, c
