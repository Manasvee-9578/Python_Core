str = """I am learning 'Python'"""
print(str)

s = "welcome to core python"
print(s)
print(s[0])
print(s[2:6])
print(s[11:])
print(s[-1])
print(s* 2)
print(s + " programming")
print(len(s))
print(s.upper())
print(s.lower())    
print(s.capitalize())
print(s.title())
print(s.count('o'))
print(s.find('core'))
print(s.replace('core', 'advanced'))
print(s.split(' '))

#to understand byte type arrays and bytearray type arrays
ele = [65, 66, 67, 68, 69]
x = bytes(ele)
print
for i in x:
    print(i)

x = bytearray(ele)
x[0] = 97
print(x)
for i in x:
    print(i)


str2 = "india"
print(str2.islower())
print(str2.isupper())
print(str2[2].isupper())

print(3*"Hii")