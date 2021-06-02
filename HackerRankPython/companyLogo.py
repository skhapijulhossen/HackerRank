if __name__ == '__main__':
    s = input().lower()
    char_counter =dict()
    for char in sorted(s):
        if char in char_counter.keys():
            char_counter[char] +=1
        else:
            char_counter[char] =1
    sort_byVal =sorted(char_counter.values(),reverse=True)
    top=3
    print(char_counter)
    for val in sort_byVal:
        for char in char_counter.keys():
            if char_counter[char] == val:
                print(char+" "+str(val))
                char_counter.pop(char)
                top-=1
                break
        if top==0:
            break
