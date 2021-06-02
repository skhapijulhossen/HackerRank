import numpy
N= int(input())
A = numpy.array([list(map(int,input().split())) for n in range(N)]);B = numpy.array([list(map(int,input().split())) for n in range(N)])
print(numpy.dot(A,B))
# for i in range(N):
#     mul =0
#     for j in range(N):
#         mul += A[i][j] * B[j][i]
#     print(mul)
    