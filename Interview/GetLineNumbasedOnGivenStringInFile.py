f = open('file1','r')
i = input("Enter str to find line num:")
line_num = 0
for line in f.readline():
    line_num+=1
    if line.find(i):
        print(line_num)


