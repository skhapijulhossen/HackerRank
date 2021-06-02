cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibbo =[]
    a,b = 0,1
    if n ==1:
        fibbo.append(a)
        return fibbo
    elif n == 2:
        fibbo.extend([a,b])
        return fibbo
    while len(fibbo) < n:
        fibbo.append(a)
        a, b = b, a+b
    return fibbo

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))