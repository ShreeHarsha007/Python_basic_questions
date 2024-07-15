from array import *

# in python we need to import arrays and then code or use them 

a = [87, 67, 99, 99]
b = [4,5,6,45,6,4,6,45,54,-65]
print(a+b)
val = array('i',[4,5,6,45,6,4,6,45,54,-65])

# for i in (val):
print(val.buffer_info()) 

# //////////////////////////////////////////////////////////////////////////////////

arr = array('i',[])

n = int(input("Enter the array size:"))

for i in range(n):
    x = int(input("Enter the number :"))
    arr.append(x)

print(arr)