# Convert a float to an integer
x = 12.33
print(int(x))

# Convert an integer to a float
y = 45
print(float(y))

#Convert integer to complex number
z = 5
print(complex(z))
a = 3
b = -5
print(complex(a, b))

# Convert binary, hexadecimal, and octal numbers to integers
n1 = 0b1010
print(int(n1)) 

n2 = 0x1A
print(int(n2))

n3 = 0o25
print(int(n3))

#Convert string representations to integers
str = "1c2"
n = int(str, 16)
print(n)

#Convert into decimal number system
s1 = "17"
s2 = "1110010"
s3 = "1c2"
n = int(s1, 8)
print("Octal of 17 is:", n)
n = int(s2, 2)
print("Binary of 1110010 is:", n)
n = int(s3, 16)
print("Hexadecimal of 1c2 is:", n)

#Convert integer to binary, hexadecimal, and octal representations
A = 10
print(bin(A))   # binary representation
print(hex(A))   # hexadecimal representation    
print(oct(A))   # octal representation