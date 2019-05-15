a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

intersection = set(a.keys() & b.keys())
print(intersection)

newlist = []
for k in b.keys():
    if k not in a.keys():
        newlist.append(k)
print(newlist)

print(dict((x, a.get(x, 0) + b.get(x, 0)) for x in set(a) | set(b)))
