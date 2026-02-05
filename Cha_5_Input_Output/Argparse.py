import argparse 
parser = argparse.ArgumentParser(description='This program displays the square value of given number') 
parser.add_argument("num", type=int, help="Please input integer type  number.") 
args = parser.parse_args()
square = args.num ** 2
print(f"The square of {args.num} is {square}") #python Argparse.py 5



#A Python program to add two numbers using argument parser. 
parser = argparse.ArgumentParser(description= "This program calculates  sum of two given numbers") 
parser.add_argument("n1", type=float, help="Input first number") 
parser.add_argument("n2", type=float, help="Input second number") 
args = parser.parse_args() 
result = float(args.n1)+float(args.n2) 
print("Sum of two= ", result) 



#To accept 2 arguments and display the first number and its power.
parser.add_argument('nums', nargs=2) 
args = parser.parse_args() 
print('Number= ', args.nums[0]) 
print('Its power= ', args.nums[1]) 
result = float(args.nums[0])** float(args.nums[1]) 
print('Result= ', result)


#To accept 1 or more arguments and display them as list elements. 
parser = argparse.ArgumentParser() 
parser.add_argument('nums', nargs='+') 
args = parser.parse_args() 
for x in args.nums: 
    print(x) 