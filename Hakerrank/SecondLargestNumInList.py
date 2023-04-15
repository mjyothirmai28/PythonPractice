# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains n . The second line contains an array A[]  of n integers each separated by a space.
# n = int(input())
# arr = [1,2,3,4,2]
# # print(arr.sort())
# arr.remove(max(arr))
# print(max(arr))
# # for i in arr:
#     print(i)
# n = int(input())
# arr = [1,3,4,2,5]
# arr.sort()
# print(arr[-2])
n = int(input())
arr = [1,3,4,5,2,5]

SET=set(sorted(arr))
List=sorted(SET)
print(List[-2])