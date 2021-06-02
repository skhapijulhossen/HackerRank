# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
code =[]
for line in range(int(input())):
    state = input()
    if bool(re.match(r'^[a-z]', state)):
        state = re.sub(r'[\s]+[&]{2}[\s]+', ' and ',state)
        state = re.sub(r'[\s]+[|]{2}[\s]+', ' or ',state)
        code.append(state)
    else:
        code.append(state)
print('\n'.join(code))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = []
def change(match):
    if match.group(0) == '&&':
        return 'and'
    elif  match.group(0) == '||':
        return 'or'
    
    
N = input()
for i in range(int(N)):
    T.append(input())
    
match = '\n'.join(T)

print(re.sub(r"(?<= )(&&|\|\|)(?= )", change,match))
    