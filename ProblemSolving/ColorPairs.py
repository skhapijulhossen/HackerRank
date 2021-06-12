def sockMerchant(n, ar):
    # Write your code here
    counter = 0
    for color in set(ar):
        counter += (ar.count(color) // 2)
        
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()