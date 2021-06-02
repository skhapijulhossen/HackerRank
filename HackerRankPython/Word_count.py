# Enter your code here. Read input from STDIN. Print output to STDOUT
words_count = dict()
for i in range(int(input())):
    word = input()
    if word in words_count.keys():
        words_count[word] += 1
    else:
        words_count[word] = 1
print(len(words_count))
print(' '.join([str(x) for x in words_count.values()]))