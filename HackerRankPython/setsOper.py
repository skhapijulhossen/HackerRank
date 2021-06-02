n1 = int(input())
M = set(map(int, input().split()))
n2 = int(input())
N = set(map(int, input().split()))
diff = list(M.difference(N))
diff.extend(list(N.difference(M)))
for elem in sorted(diff):
    print(elem)