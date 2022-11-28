# Get the values of a, b and c (coefficients of quadratic equation) as input from the user and calculate
# the roots and print as the output

import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

D = (b * b) - (4 * a * c)

if D > 0:
    root1 = ((-b) + math.sqrt(D)) / (2 * a)
    root2 = ((-b) - math.sqrt(D)) / (2 * a)
    print('roots are real and unequal')
    print('root1', root1, '\nroot2 = ', root2)

elif D == 0:
    root1 = ((-b) + math.sqrt(D)) / (2 * a)
    print('roots are equal')
    print('root1 = root2 = ', root1)

elif D < 0:
    root_real = (-b) / (2 * a)
    root_imag = math.sqrt(-D) / (2 * a)
    print('roots are not real')
    print('root1 = ', root_real, '+', root_imag,'i')
    print('root2 = ', root_real, '-', root_imag,'i')
