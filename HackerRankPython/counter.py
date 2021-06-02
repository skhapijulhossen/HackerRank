from collections import Counter

sizesCount = int(input())
sizes = Counter(map(int, input().split(' ')))
purchases =map(tuple, [map(int, input().split(' ')) for _ in range(int(input()))])
money_earned = 0

for purchase in purchases:
    if purchase[0] in sizes.keys() and sizes[purchase[0]]:
        sizes[purchase[0]] -=1;money_earned += purchase[1]



print(money_earned)

