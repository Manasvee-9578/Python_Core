print(2*"hii")

a, b = 2, 4
print(a, b)

print(a, b, sep="---")

print("hello", end=" ")
print("how are you?", end=" ")
print("I am fine.", end="\n\n")
print("This is printed on a new line.", end="\t")

m = 2
print(m, "is even number.")
print("you typed",m , "as input.")

x=10 
print('value= %i' %  x) 
 

x, y = 10, 15 
print('x= %i y= %d' % (x, y)) 

name = "India"
print('Hai %s' % name) 
print('Hai (%20s)' % name) 
print('Hai (%-20s)' % name) 

print('Hai %c, %c' % (name[0], name[1])) 
print('Hai %s' %(name[0:2])) 


num=123.456789 
print('The value is: %f' % num)  
print('The value is: %8.2f' %num) 
print('The value is: %.2f' %num) 


name, salary = 'Ravi', 12500.75 
print('Hello {0}, your salary is {1}'.format(name, salary)) 
 
print('Hello {n}, your salary is {s}'.format(n=name, s=salary)) 
 
print('Hello {:s}, your salary is {:.2f}'.format(name, salary)) 
 
print('Hello %s, your salary is %.2f' % (name, salary)) 
