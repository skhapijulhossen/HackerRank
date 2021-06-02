# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()
pattern =input()
matches = re.search(r'{}'.format(pattern), string)
print(matches.end())