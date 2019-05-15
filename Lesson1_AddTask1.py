list1 = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

max_value = max(list1)
maxIndexList = [index for index, value in enumerate(list1) if value == max(list1)]
print(max_value, maxIndexList)
min_value = min(list1)
minIndexList = [index for index, value in enumerate(list1) if value == min(list1)]
print(min_value, minIndexList)
from collections import Counter

count = Counter(list1)
threemaxcount = []
threemaxcount = count.most_common()[:3]
print(threemaxcount)

newlist, newlist1 = [], []

for i in list1:
    if i not in newlist:
        newlist.append(i)
print(newlist)
list1.sort()
for i in list1:
    if i not in newlist1:
        newlist1.append(i)
print(newlist1)
