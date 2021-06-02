from collections import OrderedDict
purchases_count =int(input())
details = OrderedDict()
for i in range(purchases_count):
    info = input().split()
    if ' '.join(info[:-1]) in details.keys():
        details[' '.join(info[:-1])] += int(info[-1])
    else:
       details[' '.join(info[:-1])] = int(info[-1])
for item_name, net_price in details.items():
    print(f'{item_name} {net_price}')