import sys
n = len(sys.argv)   # python Command_line_arg.py 10 manasvee 22.3
args = sys.argv   
print('No. of command line args= ', n) 
print('The args are: ', args) 
print('The args one by one: ') 
for a in args: 
    print(a) 
 
