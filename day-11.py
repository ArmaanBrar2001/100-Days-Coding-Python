# Fibonacci series is a special series where nth term is the sum of previous two terms in the series. The
# series starts with 0 and 1 as the first and second term of the series respectively.
# Here you need to get the value for nth term from user and then print Fibonacci series containing n terms.

a = int(input())


# def fib(n):
#     if n == 0 or n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return (fib(n - 1) + fib(n - 2))

first = 0
second = 1

for i in range(a):
    print(first)
    third = first + second
    first = second
    second = third
