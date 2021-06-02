#!/bin/python3

def timeConversion(s):
    # Write your code here
    am = 1 if s[-2:] == 'AM' else 0
    if am:
        s_arr = s.split(':')
        s_arr[0] = '00' if s_arr[0] == '12' else s_arr[0]
        return ":".join(s_arr)[:-2]
    else:
        s_arr = s.split(':')
        s_arr[-1]= s_arr[-1][:2]
        clock_24 = int(s_arr[0])%12
        s_arr[0] =str(clock_24+12)
        return ":".join(s_arr)


print(timeConversion("12:40:22AM"))