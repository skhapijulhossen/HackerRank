# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
digits = [int(digit) for digit in string if digit.isdigit()]
upper = sorted([ upp for upp in string if upp.isupper()])
lower = sorted([ upp for upp in string if upp.islower()])
even = list(map(str,sorted(list(filter(lambda d:d%2==0, digits)))))
odd = list(map(str, sorted(list(filter(lambda d:d%2!=0, digits)))))
alll = lower+upper+odd+even
print(''.join(alll))
