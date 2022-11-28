# Get a number from user for which you need to fin the factorial, then calculate the factorial and give it
# as the output.

a = int(input())


def fact(n):
    if n == 1 or n == 0:
        return 1

    else:
        return n * fact(n - 1)


print(fact(a))
