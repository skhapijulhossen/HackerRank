# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
ValidNumbers =[]
for number in range(int(input())):
    if re.match(r'^[789]+\d{9,9}$', input().rstrip()):
        ValidNumbers.append('YES')
    else:
        ValidNumbers.append('NO')
print('\n'.join(ValidNumbers))