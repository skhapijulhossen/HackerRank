
def f(n):
    def factorial(n):
        if n > 1:
            return n*factorial(n-1)
        else:
            return 1
    digits = list(map(int, list(str(n))))
    summ = 0
    for digit in digits:
        summ += factorial(digit)
    return summ
def sf(n):
    summ = f(n)
    digits = list(map(int, list(str(summ))))
    return sum(digits) 



print(sf(25))