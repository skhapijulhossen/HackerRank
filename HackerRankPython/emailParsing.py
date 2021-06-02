import  email.utils as eu
validEmails = []
for emai in range(int(input())):
    email= input()
    if eu.re.match(r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$' eu.parseaddr(email)[1]):
        validEmails.append(email)
print('\n'.join(validEmails))