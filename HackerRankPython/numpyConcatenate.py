import numpy
N,m,p =list(map(int, input().split()))
narray = numpy.array([input().split() for i in range(N)], int)
marray = numpy.array([input().split() for i in range(m)], int)
print(numpy.concatenate((narray,marray), axis=0))

numpy