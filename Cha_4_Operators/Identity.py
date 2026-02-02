a = 10;b=12
print(id(a))
print(id(b))

x = 143; y = 143
if(x is y):
    print("x and y are same")
else:   
    print("x and y are not same")

name = "manasvee"
userid = "manasvee"
if(name is not userid):
    print("name and userid are same")
else:   
    print("name and userid are not same")

one = [1,2,3,4] 
two = [1,2,3,4] 
if(one is two): 
    print("one and two are same") 
else: 
    print("one and two are not same")

if(one == two): 
    print("one and two are same") 
else: 
    print("one and two are not same")