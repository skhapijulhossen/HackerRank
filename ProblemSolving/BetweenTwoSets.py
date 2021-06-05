def getTotalX(a, b):
    # Write your code here
    low = a[-1]
    mid_vals = []
    while low<=b[0]:
        if all([ True if low%e==0 else False for e in a]):
            divide = all([True if elem%low==0 else False for elem in b])
            if divide:
                mid_vals.append(low)
        low += 1
    return len(mid_vals)