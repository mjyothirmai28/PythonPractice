def secondLowestSorted(arr):
    val = 0
    for i in arr:
        if(i != arr[0]):
            val = i
    return val

stu = {}
for _ in range(5):
    name = input()
    score = float(input())
    stu[name] = score
# print(stu)
val_list = list(stu.values())
key_list = list(stu.keys())
# print(key_list.sort())
# key_sorted = sorted(key_list)
# print(key_sorted)

# print key with val 100
# position = val_list.index(2)
# print(key_list[position])
# print(val_list)
# print(key_list)
set1 = set(val_list)
sortedset1 = sorted(set1)
# print(sortedset1)
# print(sortedset1[1])
# Sorting the  list
#val_list.sort()
# Printing the second last element
#print("Second lowest element is:", val_list[1])
#print(val_list)
keys = [k for k, v in stu.items() if v == sortedset1[1]]
# keys = [k for k, v in stu.items() if v == val_list[1]]
#keys = [k for k, v in stu.items() if v == secondLowestSorted(val_list)]
for item in sorted(keys):
    print(item)
# for item in keys:
#     print(item)
# for key in sorted(stu.keys()):
#     print(key)
       # print("%s: %s" % (key, stu[key]))
#print(keys)
#print(*keys)


