def sockMerchant(n, ar):
    # Write your code here
    counter = 0
    for color in set(ar):
        counter += (ar.count(color) // 2)
        
    return counter
