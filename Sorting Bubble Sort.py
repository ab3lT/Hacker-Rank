def conutSwaps(a):
    s = 0
    for i in range(len(a)-1):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                s += 1
    print(f"Array is sorted in numSwaps {s} swaps.")
    print(f"First Elemnt: {a[0]}")
    print(f"Last Element: {a[-1]}")

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'countSwaps' function below.
# #
# # The function accepts INTEGER_ARRAY a as parameter.
# #

# def countSwaps(a):
#     s = 0
#     for i in range(len(a)-1):
#         for j in range(i, len(a)):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#                 s += 1
#     print(f"Array is sorted in {s} swaps.")
#     print(f"First Element: {a[0]}")
#     print(f"Last Element: {a[-1]}")
    
# if __name__ == '__main__':
#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

#     countSwaps(a)
