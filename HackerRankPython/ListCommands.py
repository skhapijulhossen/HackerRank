if __name__ == '__main__':
    N = int(input())
    list_ =[]
    for op in range(N):
        operation = input().lower().split(' ')
        if operation[0] =='insert':
            list_.insert(int(operation[1]), int(operation[2]))
        elif len(operation) == 1:
            if operation[0] == 'print':
                print(list_)
            elif operation[0] == 'sort':
                list_ =sorted(list_)
            elif operation[0] == 'pop':
                list_.pop()
            else:
                list_ =list_[::-1]
        else:
            if operation[0] == 'remove':
                list_.remove(int(operation[1]))
            else:
                list_.append(int(operation[1]))

