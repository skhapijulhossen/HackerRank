def divisibleSumPairs(n, k, ar):
    # Write your code here
    return sum([1 for i in range(n) for j in range(i, n) if (ar[i]+ar[j])%k == 0 and i<j])