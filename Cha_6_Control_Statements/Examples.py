# N = int(input("How many Fibonacci numbers do you want? "))
# f1 = 0
# f2 = 1
# c = 2
# if N == 1:
#     print(f1)
# elif N == 2:
#     print(f1,"\n",f2,sep="")
# else:
#     print(f1,"\n",f2,sep="")
#     while c < n:
#         f = f1 + f2
#         print(f)
#         f1 = f2
#         f2 = f
#         c += 1

import math as m
x, n = [int(i) for i in input("Enter angle value, no. of iterations:  ").split(',')]
r=(x*3.14159)/180 
t=r 
sum=r 
print('Iteration= %d\tSum= %f' % (1, sum)) 
i=2 
for j in range(2, n+1): 
    t=(-1)*t*r*r/(i*(i+1))  
    sum=sum+t;  
    print('Iteration= %d\tSum= %f' % (j, sum)) 
    i +=2  