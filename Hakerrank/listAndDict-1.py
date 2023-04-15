if __name__ == '__main__':
    stu = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu[name] = score
val_list = list(stu.values())
key_list = list(stu.keys())
set1 =set(val_list)
sortedset1 = sorted(set1)
secondHighestValue = sortedset1[1]
keys = [k for k, v in stu.items() if v == secondHighestValue]
for item in sorted(keys):
    print(item)