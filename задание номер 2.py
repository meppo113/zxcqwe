import random
list = [1,2,3,4,5,6,7,8,9,0]
a=""
b=""
c=""
for i in range(4):
    a+=str(random.choice(list))
    b+= str(random.choice(list))
    c += str(random.choice(list))
print(a,b,c, sep=":")
print(a,b,c, sep=".")