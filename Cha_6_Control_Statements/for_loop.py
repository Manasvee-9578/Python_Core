str = "hello i am manasvee"
for ch in str:
    print(ch)

n = len(str)#--> 0 to n-1
for i in range(n):
    print(str[i])
print()

for i in range(1, 11):
    print(i)

for i in range(2, 101 , 2):
    print(i)
print("Even numbers from 1 to 100")

for x in range(10, 0, -1):
    print(x)

lst = [10.5,"manasvee","23DCS143",143]
for element in lst:
    print(element)

list = [10, 20, 30, 40, 50]
sum = 0
for i in list:
    sum += i
print("Sum of the list is:", sum)

list1 = [1, 2, 3, 4, 5]
sum = 0
i = 0
while i< len(list1):
    sum += list1[i]
    i += 1
print("Sum of the list is:", sum)