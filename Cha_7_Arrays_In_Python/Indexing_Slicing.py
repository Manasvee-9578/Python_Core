from array import *

x = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
n = len(x)
for i in range(n):
    print(x[i], end=' ')
print()
i = 0
while i<n:
    print(x[i], end=' ')
    i += 1
print()

for i in x[2:5]:
    print(i, end=' ')
print()

y = x[1:10:2]
print("\n", y)

z = x[0:]
print("\n",z)

a = x[:5]
print("\n",a)

b = x[::2]
print("\n",b)

c = x[1::2]
print("\n",c)

d = x[-4:]
print("\n",d)

x[1:10] = array('i',[100,200])
print("\n",x)