import array as arr

a1 = arr.array('i', [1, 2, 3, 4, 5])
print(a1)
b = arr.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])
print(b)
c = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
print(c)
d = arr.array('B', [1, 2, 3, 4, 5])
print(d)
print("Elements of array a:")
for i in a1:
    print(i)
print()

arr1 = arr.array(a1.typecode,(a for a in a1))
print(arr1)
arr2 = arr.array(a1.typecode,(a * 3 for a in a1))
print(arr2)