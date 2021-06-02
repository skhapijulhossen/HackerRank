# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^[+-]?\d*?\.{1}\d+$'
N = int(input())
for case in range(N):
    print(bool(re.match(pattern, string=input())))