a = "My name is jyothirmai"
count = {}
for eachchar in a.lower():
    count.setdefault(eachchar, 0)
    #sorted(count)
    count[eachchar] = count[eachchar] +1
print(count)
x=sorted(count.items())

print(x)