noOfEnglishSub =int(input());EngSub = set(list(map(int, input().split())))
noOfFrenchSub =int(input());FrenchSub = set(list(map(int, input().split())))
print(len(EngSub.union(FrenchSub)))

noOfEnglishSub =int(input());EngSub = set(list(map(int, input().split())))
noOfFrenchSub =int(input());FrenchSub = set(list(map(int, input().split())))
print(len(EngSub.difference(FrenchSub)))