def factorial(n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n - 1)

def sum(n):
    if n == 1:
        result = 1
    else:
        result = n + sum(n - 1)

    return result

def length(str):
    if str == "":
        return 0
    else:
        return 1 + length(str[1:])

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

def fibonnaci(n):
    if n <= 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def main():

    print(fibonnaci(40))
    #print(fibonnaci(40))
    #print(fibonnaci(45))
    '''print(power(5,3))
    print(power(2, 10))
    print(length('abc'))
    print(length("1234567890"))
    print(factorial(5))
    print(factorial(10))
    print(sum(10))
    print(sum(100))'''

main()
