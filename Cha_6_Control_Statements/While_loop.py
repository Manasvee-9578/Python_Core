x = 1
while x <=10:
    print(x)
    x += 1
    print("Inside loop")
print("Loop ended")

m = int(input("enter minimum range value:"))
n = int(input("enter maximum range value:"))
X = m
if X % 2 == 0:
    print(X, "is even")
else:
    print(X, "is odd")
while X <= n and X>=m:
    print(X)
    X+=2