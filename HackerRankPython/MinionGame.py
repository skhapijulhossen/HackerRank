def minion_game(string):
    vowels_list = set(['A','E','I','O','U'])
    consonants = 0
    vowels = 0
 
    n = len(string)
    for i, l in enumerate(string):
        if l in vowels_list:
            vowels += n-i
        else:
            consonants += n-i
 
    if vowels == consonants:
        print("Draw")
    elif vowels > consonants:
        print("Kevin {}".format(vowels))
    else:
        print("Stuart {}".format(consonants))

print(tuple(enumerate('BANANA')))