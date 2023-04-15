# message = 'python is popularpo programming language'
#
# # number of occurrence of 'p'
# print('Number of occurrence of given string is:', message.count(input()))

def count_substring(string, sub_string):
    # number of occurrence of 'p'
    #print(string.count(sub_string))
    total = 0
    for i in range(len(string)):
        if string[i: i + len(sub_string)] == sub_string:
            total += 1
    return total
        #print(string[i])
        #return string.count(sub_string)
    #return string.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


#output
# ABCDCDC
# CDC