ints_list = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
ints_list.sort()
temp =[]
[temp.append(i)
for i in ints_list
    if i not in temp]
print (temp)
