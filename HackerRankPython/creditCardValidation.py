import re
for test in range(int(input())):
    card_number = input()
    not_ep_div = all([False for div in card_number.split('-') if len(div)!=4])
    without = card_number.replace('-','')
    len_total = len(without) == 16
    starts_with = re.match(r'^4|5|6',without)
    contains = re.match(r'[0-9]{16}', without)
    # reduce()

    

    