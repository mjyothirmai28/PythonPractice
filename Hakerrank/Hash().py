if __name__ == '__main__':
    n = int(input())  #asks user how many nums in list
    integer_list = map(int, input().split()) # asks user to give list
    print(hash(tuple((integer_list)))) # change Existing list to tuple and print hash of that tuple

# n = 2
#integer_list = 1 2
#hash(tuple((integer_list))) = 3713081631934410656