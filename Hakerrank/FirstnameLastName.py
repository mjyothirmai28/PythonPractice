#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
#ol = ["Hello ","" ," ","", " " ," !You just delved into python. "]
ol = ["Hello ", ""," " , "","!"," You just delved into python."]
def print_full_name(first, last):
    # ol.append(first)
    # ol.append(last)
    # ol.insert(1,first)
    # ol.insert(2,last)
    ol[1] = first
    ol[3] = last
    print("".join(ol))
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    #print(result)

#Hello firstname lastname! You just delved into python.

# Ross
# Taylor
# Hello Ross Taylor! You just delved into python.
