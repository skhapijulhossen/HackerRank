import re
import email.utils
N = input()
p = [ email.utils.parseaddr(input()) for emails in range(int(N))]
for em in p:
    if re.match(r'^[a-z]{1}[\w._-]+@[a-z]+[.]+[a-zA-Z]{1,3}$', em[1]):
        print(email.utils.formataddr(em))      
    else:
        pass