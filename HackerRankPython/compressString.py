from itertools import groupby
for key, occurences in groupby(input()):
    print((int(key),len(list(occurences))),end=' ')