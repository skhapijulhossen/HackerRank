import re
pattern = re.compile(r'#[a-fA-F0-9]{3,6}')
inside = False
for code in range(int(input())):
    proprties = input()
    if "{" in  proprties:
        inside =True
    elif "}" in proprties:
        inside = False
    elif inside:
        for code in re.findall(pattern, proprties):
            print(code)
