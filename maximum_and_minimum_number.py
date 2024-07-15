# def maximum_number(numbers):
#     if not numbers:
#         return None
#     max_value = numbers[0]
#     min_value = numbers[0]

#     for num in numbers:
#         if num > max_value:
#             max_value = num 
#         elif num < min_value:
#             min_value = num 

#     return max_value, min_value

# numbers = [5,4,5435,436,3443,43,6436,43043,634,65643,353]

# max_value, min_value = maximum_number(numbers)

# print(max_value)
# print(min_value)


def fibo():
    a,b =0,1
    while True:
        yield a
        a,b =b, a+b

f1 = fibo()
print(f1)
