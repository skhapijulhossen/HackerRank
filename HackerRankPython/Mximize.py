# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = list(map(int, input().split()))
MAX =[]
for line in range(K):
    elements = list(map(int, input().split()))
    MAX.append(map(lambda x: x**2%M, elements))
 
print(max(map(lambda x: sum(x)%M, product(*MAX))))