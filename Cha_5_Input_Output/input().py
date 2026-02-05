str0 = input()
print(str0)

str1 = input("Enter your name: ")
print(str1)

str = input('Enter a number: ') 
a =  int(str) 
print(a) 

b = int(input('Enter a number: ')) 
print(b) 

c = float(input('Enter a number: ')) 
print(c) 
 
ch = input("Enter a char: ") 
print("You entered: "+ch)
print("entered: "+ch[0]) 
 
d = int(input('Enter a number: ')) 
print('entered: ', d)

e = int(input('Enter first number: ')) 
f = int(input('Enter second number: ')) 
print('U entered: ', e, f) 

print('U entered: ', e, f, sep=',')

print('U entered: %d, %d' %(e, f)) 

g = int(input("Enter first number:"))
h = int(input("Enter second number:"))
print("Sum of",g,"and",h,"is:", g+h)

i = int(input("Enter the 1st value:"))
j = int(input("Enter the 2nd value:"))
print("Sum of ",i,"and",j,"is:",i+j)
print("Product of",i,"and",j,"is:",i*j)

# input from other number systems 
str = input('Enter hexadecimal number: ')  # accept input as string 
n = int(str, 16)  # inform the number is base 16 
print('Hexadecimal to Decimal= ', n); 
 
str = input('Enter octal number: ') 
n = int(str, 8)  # inform the number is base 8 
print('Octal to Decimal= ', n); 
 
str = input('Enter binary number: ') 
n = int(str, 2)  # inform the number is base 2 
print('Binary to Decimal= ', n); 


A , B = [int(X) for X in input("Enter two numbers: ").split()] # multiple inputs in single line
print("You entered: ", A, B)

var1, var2, var3 = [int(x) for x in input("Enter three numbers: ").split(",")] 
print('Sum = ', var1+var2+var3) 

lst = [x for x in input("enter strings you want in list:").split(",")]
print("List is:", lst)

a1 ,b1 = 5, 10
result = eval("a1+b1-4")
print(result)

x1 = eval(input("Enter an expression:"))
print("Result:%d"%x1)

lst1 = eval(input("enter a list:"))
print("list:",lst1)#input = ["ma","na","sv","ee"]

tpl = eval(input("Enter a tuple: ")) #input=(10, 20, 30, 40)
print("Tuple= ", tpl) 

