#Input
# 2
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
#Output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
# N = [1,2,3,5,4,8,6]
# print(N)
# #o = input("enter operation to perform")
# for iter in range(N):
#     queryList = input().split()
#     if queryList == "insert":
#         N.insert(int(input()),int(input()))
#
#     elif queryList == "append":
#         N.append(input())
#     elif queryList == "remove":
#         N.remove(int(input()))
#     elif queryList == "sort":
#         N.sort()
#     elif queryList == "pop":
#         N.pop(int(input()))
#     elif queryList == "reverse":
#         N.reverse()
#     elif queryList == "print":
#         print(N)
#
#
# #print(N)
# #N.append(8)
#
# # if queryList == append:
# #     N.append(n)
if __name__ == '__main__':
    N = int(input())
    list1 = []
    for iter in range(N):
        queryList = input().split()
        if queryList[0] == 'insert':
            list1.insert(int(queryList[1]),int(queryList[2]))

        elif queryList[0] == 'print':
            print(list1)

        elif queryList[0] == 'remove':
            list1.remove(int(queryList[1]))

        elif queryList[0] == 'append':
            list1.append(int(queryList[1]))

        elif queryList[0] == 'sort':
            list1.sort()

        elif queryList[0] == 'pop':
            list1.pop()

        elif queryList[0] == 'reverse':
            list1.reverse()

