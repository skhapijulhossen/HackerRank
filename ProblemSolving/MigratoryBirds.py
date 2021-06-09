from collections import Counter

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    counter = sorted([(key, value) for key, value in Counter(arr).items()],key=lambda x:x[1], reverse=True)
    maxx = counter[0][1]
    return min([bid for bid,count in counter if count==maxx])

print(migratoryBirds([1,2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))