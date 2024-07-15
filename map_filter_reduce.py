from functools import *
nums = [3,45,35,35,43252,435,452,345,345,4352,4352,435,43,5432,543,52,43,532]

evens = list(filter(lambda a: a % 2 == 0, nums))  # Here the nums are taken and filtered based on condition
print(evens)                                        

doubles = list(map(lambda a: a * 2, evens)) # the nums are taken from evens and maps 2 to all the numbers making them double
print(doubles)
sum = reduce(lambda a , b: a + b, doubles)  # the nums are taken from the doubleas and reduce from by adding them 
                                            #  all one by one

print(sum)


