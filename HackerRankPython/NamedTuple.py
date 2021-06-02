from collections import namedtuple
no_stud = int(input());cols = input().split()
Student = namedtuple('Student',','.join(cols))
summ =0
for i in range(no_stud):
    info = input().split()
    stud =Student(*info)
    summ += int(stud.MARKS)
print(round((summ/no_stud), 2))