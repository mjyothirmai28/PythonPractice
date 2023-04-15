import math
l1 = [1,2,3]
add = 0
for each_ele in l1:
    add += each_ele
print(add)
avg = float(add/len(l1))
print(f"{avg:.2f}")