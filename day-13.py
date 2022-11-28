# Get the input from the user for the value of n and then find the sum of first n natural numbers.

a = int(input())
s = 0


for i in range(1, a + 1):
    s += i

print(s)
