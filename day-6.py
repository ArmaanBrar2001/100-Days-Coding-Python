# Get the value of x and y coordinates as input from the user and check in which quadrant the point lies
# and print it.

x = int(input('Enter x-coordinate: '))
y = int(input('Enter y-coordinate: '))

if x > 0 and y > 0:
    print('First Quadrant')
elif x < 0 and y > 0:
    print('Second Quadrant')
elif x < 0 and y < 0:
    print('Third Quadrant')
elif x > 0 and y < 0:
    print('Fourth Quadrant')
elif x == 0 and y == 0:
    print('Origin')
