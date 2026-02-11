for i in range(3):
    for j in range(4):
        print("i=",i,"\t","j=",j)

for i in range(1,11):
    for j in range(1, i+1):
        print("*",end="")
    print()  # Move to the next line after inner loop
 
n=40 
for i in range(1, 11): 
    print(' '*n, end='')  # repeat space for n times 
    print ('* '*(i))  # repeat star for i times 
    n-=1 

for i in range(1,11):
    print(""*(n-i)+"*"*(i))

for x in range(1,101):
    for y in range(1,11):
        print('{:8}'.format(x*y), end='') #8 spaces for each number
    print()

