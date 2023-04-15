#final = []
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    #print(line)

    # for eachele in line:
    #     if eachele==" ":
    #         cond = "-"
    #         #final.append(cond)
    #
    #     else:
    #         #final.append(eachele)
    #         print(eachele)
    # return "".join(line)
# write your code here

#this is a string(Input)
#this-is-a-string(output)


#My Name is Jyo

# a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:
#
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string