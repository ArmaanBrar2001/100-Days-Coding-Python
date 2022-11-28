# Get a number from user and then find the sum of the digits in the given number.

a = int(input())
s = 0

while a > 0:
    rem = a % 10
    s += rem
    a = int(a / 10)

print(s)
