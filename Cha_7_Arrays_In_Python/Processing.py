from array import *

a = array('i',[2,4,6,7,8,4,3,8,6,4,7,9,5,3,2,1,0])
print(a,end='')
print()

print("\n",a.append(10),end='')

print("\n",a.count(4),end='')

print("\n",a.extend([11,12,13]),end='')

# print("\n",a.fromfile('data.txt'),end='') --> reads data from a file and appends to the array

print("\n",a.fromlist([14,15,16]),end='')

print("\n",a.index(8),end='')

print("\n",a.insert(2,20),end='')

print("\n",a.pop(0),end='')

print("\n",a.remove(4),end='')

print("\n",a.reverse(),end='')

#print("\n",a.tofile('data.txt'),end='') --> writes the array data to a file

print("\n",a.tolist(),end='')

# print("\n",a.tostring{},end='') --> converts the array to a string representation

print("\n",a.typecode,end='')

print("\n",a.itemsize, end='')
