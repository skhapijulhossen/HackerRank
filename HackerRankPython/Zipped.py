N , x = map(int,input().split())
marks =[]
for subject in range(x):
    marks += [list(map(float,input().split()))]
zipped = list(zip(*marks))
for subMarks in zipped:
    print(round(sum(subMarks)/x,1))