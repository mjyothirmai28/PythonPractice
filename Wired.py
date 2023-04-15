import math
import os
import random
import re
import sys



if __name__ == '__main__':
   # n = int(input().strip())
   n = int(input("Enter num:"))
   # x = range(2,5)
   # y = range(6,20)
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and n in range(2,6):
    # for n in range(2,5):
    print("Not Weird")
elif n%2 == 0 and n in range(6,21):
    # for n in range(6,20):
    print("Weird")
elif n%2 == 0 and n>20:
    print("Not Weird")
print("num"/n,"num")