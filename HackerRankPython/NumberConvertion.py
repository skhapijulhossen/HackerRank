number = int(input())
w = len("{0:b}".format(number))
print(w)
for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=10))