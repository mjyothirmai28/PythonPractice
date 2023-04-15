import string

sampleInput = str(input())
split_name = [s for s in sampleInput]
#split_name.sort()
print(split_name)

small_l = [s for s in sampleInput if s.islower()]
capital_l = [s for s in sampleInput if s.isupper()]
num_l = [s for s in sampleInput if s.isnumeric()]
odd_l =[]
even_l = []
for each_ele in num_l:
    if (int(each_ele) % 2 != 0):
        odd_l.append(each_ele)
    elif (int(each_ele) == 0) or (int(each_ele) % 2 == 0):
        even_l.append(each_ele)
    # elif (int(each_ele) == 0):
    #     even_l.append(each_ele)
# sorted(small_l)
# sorted(capital_l)
small_l.sort()
capital_l.sort()
odd_l.sort()
even_l.sort()
# sorted(odd_l)
# sorted(even_l)
finalSort = small_l+capital_l+odd_l+even_l
print(finalSort)
#add_split_name = "".join([str(i) for i in split_name])
add_split_name = "".join([str(i) for i in finalSort])
print(add_split_name)
#gaGA3296
#1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM(Input)
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468(output)