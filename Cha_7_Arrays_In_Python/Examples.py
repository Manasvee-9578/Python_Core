from array import * 
# str = input('Enter marks:').split(' ') 
# marks = [int(num) for num in str] 
# sum=0 
# for x in marks: 
#     print(x) 
#     sum+=x    
# print('Total marks:', sum) 
# N = len(marks)  
# percent =  sum/N
# print('Percentage:', percent,"%") 
# print()


# from array import*  
# x = array('i', []) 
# print('How many elements? ', end='') 
# n = int(input())  
# for i in range(n):  
#     print('Enter element: ', end='') 
#     x.append(int(input())) 
# print('Original array: ', x) 

# flag = False  
# for i in range(n-1):     
#     for j in range(n-1-i):  
#         if x[j] > x[j+1]:  
#             t = x[j]  
#             x[j] = x[j+1] 
#             x[j+1] = t 
#             flag = True 
#     if flag==False: 
#         break   
#     else:  
#         flag = False  
 
# print('Sorted array= ', x)
# print()

a = array('i',[])
print('How many elements? ', end='')
l = int(input())
for i in range(l):
    print('Enter element: ', end='')
    a.append(int(input()))
print('Original array: ', a)
print("Enter a element to search: ", end='')
s = int(input())
flag = False
for i in range(l):
    if a[i] == s:
        print('Element found at index: ', i)
        flag = True
if flag == False:
    print('Element not found')
print()
#for loop or try except use one of them
try:
    pos = a.index(s)
    print('Element found at index: ', pos+1)
except ValueError:
    print('Element not found')
print()


