a = 4          # 100  3 byts
b = 5          # 101  3 byts

a = a + b   # 9 here for 9 we neeed 1001  4 byts  we are wasting one extra byt
b = a - b     # soto avoid that we use Xor because Xor doesnot uses extra space.

a = a - b

print(a,b)

# ////////////////////////////////////////

a = 4
b = 5

temp = a
a = b
b = temp

print(a,b)

# //////////////////////////////////////////

a = 4
b = 5

a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)

# ///////////////////////////////////////////
a = 4
b = 5                            # rot_two()  , function in python.
a,b = b,a
print(a,b)