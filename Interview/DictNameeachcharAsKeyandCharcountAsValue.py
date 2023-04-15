# name = "Jyothirmai"
# nl = list(name)
# for eachletter in nl:
#     print(eachletter, end=" ")
#     print(nl.count(eachletter))
# print(dict[eachletter,nl.count(eachletter)])
o = "Jyothirmai"
ed = {}
for eachchar in o:
    ed[eachchar] = ed.get(eachchar,0)+1
print(ed)