for inputs in range(int(input())):
    no_qubes = int(input());cubes = list(map(int, input().split()));j=-1;response='Yes';responses=[]
    for i in range(no_qubes//2):
        j-=1
        if cubes[i] < cubes[j]:
            responses.append('No');break
    responses.append(response)
print('\n'.join(responses))
            