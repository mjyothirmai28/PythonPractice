l1 = ["a","b","c",1,2,3]
alpha = []
num = []
for eachele in l1:
    if str(eachele).isalpha():
        alpha.append(eachele)
    elif str(eachele).isnumeric():
        num.append(eachele)
print(alpha)
print(num)
print(dict(zip(alpha,num)))
