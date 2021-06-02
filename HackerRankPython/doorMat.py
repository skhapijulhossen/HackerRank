N, M = map(int, input().split(' '))
for f in range(N// 2):
    i=3
    print(('.|.' * f).rjust((M-i)//2, '-') + '.|.' +('.|.'*f).ljust((M-i)//2,'-'))
w = N if (N-7) ==0 else N+((N-7)//2)
print('-'*w+'WELCOME'+'-'*w)
j=0
for r in range(((N-1)//2)-1, -1, -1):
    j +=3
    print(('-'*j)+('.|.'*r)+'.|.'+('.|.'*r)+('-'*j))