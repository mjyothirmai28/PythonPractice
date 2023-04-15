# m = "Jyothirma'i2"
# #sc = [x for x in m if x.isupper()]
# for eachele in m:
#     if eachele.isupper():
#         pl = eachele.lower()
#         print(pl,end="")
#     elif eachele.islower():
#         pu = eachele.upper()
#         print(pu,end="")
#     else:
#         print(eachele,end="")
# #print(pl+pu+eachele)
#
# #print(eachele.lower()+eachele.upper()+eachele)
# # m = "Jyothirma'i2"
# # s = [i for i in m ]

result = []
def swap_case(s):
    for eachele in s:
        if eachele.isupper():
            pl = eachele.lower()
            result.append(pl)
            #print(pl,end="")

        elif eachele.islower():
            pu = eachele.upper()
            result.append(pu)
            #print(pu,end="")
        else:
            result.append(eachele)
            #print(eachele,end="")
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#HackerRank.com presents "Pythonist 2".(Input)
#hACKERrANK.COM PRESENTS "pYTHONIST 2".(Output)
