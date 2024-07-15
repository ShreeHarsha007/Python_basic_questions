def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

nums = [4,34,324,23,32432,432432,32,23,5]
even = list(filter(is_even, [4,34,324,23,32432,432432,32,23,5] ))
odd = list(filter(is_odd, nums))

print("even:",even)
print("odd:" , odd)




# filter function is mainly used to filter.