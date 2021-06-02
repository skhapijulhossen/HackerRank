# Enter your code here. Read input from STDIN. Print output to STDOUT
inputs =[]
for test in range(int(input())):
    inputs.append(list(input().split()))
for nums in inputs:
    try:
        print(int(int(nums[0])/int(nums[1])))
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f"Error Code: {e}")