import re
my_str = '100.000.000,000'
# my_list = re.split(r',|.', my_str, maxsplit=3)
# print(my_list)

result = re.split(r"\D", my_str, maxsplit=3)
print(result)
for each_ele in result:
    print(each_ele)
print("\n".join(re.split(my_str, input())))