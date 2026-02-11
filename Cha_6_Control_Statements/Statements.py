l1 = [10,20,30,40,50,90,70,80,90,100]
search = int(input("Enter a number for search in list:"))
for element in l1:
    if element == search:
        print("Element found:", element)
        break
else:
    print("Element not found in the list")
print()



print("-------BREAK STATEMENT-------")
i = 0
while True:
    if i >= 3:
        break
    print(i)
    i += 1
print("loop ended")
print()



print("-------CONTINUE STATEMENT-------")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print()




print("-------PASS STATEMENT-------")
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)
print()



print("-------ASSERT STATEMENT-------")
x = int(input("Enter a positive number:"))
assert x < 0, "X should be a positive number"
print("You entered:", x)

X = int(input("Enter a positive number:"))
try:
    assert(X>0)
    print("You entered:", X)
except AssertionError:
    print("X should be a positive number")
print()




print("-------RETURN STATEMENT-------")
def add(a, b):
    print("Sum=",a+b)
    add(5, 10)
    add(1.2,5.6)
