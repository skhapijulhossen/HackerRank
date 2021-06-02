
# size = int(input())
# default = 97+size-1
# string = chr(default)

# for ch in range (size):
#     default -= 1
#     dashes = ((size-ch)-1)*2
#     string = string

#     print(string)

n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

    
