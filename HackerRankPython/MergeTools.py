def merge_the_tools(string, k):
    # your code goes here
    start = 0
    end = k
    for i in range((len(string)//k)+1):
        subs = []
        for ch in string[start:end]:
            if ch not in subs:
                subs.append(ch)
        start, end = end, end+k
        print(''.join(subs))
if __name__ == '__main__':
    # string, k = input(), int(input())
    merge_the_tools("AABCAAADA", 3)