
# def sum(sum1):
#     count = 0
#     for i in len(sum1):
#         if i > 0:
#             count = count + i
#         return count 
    
# sum1 = [3,3432,4324,234,3242,-3432,32,-32,-34]
# print(sum())

def positive_sum(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count = count + num
    return count


def main():
    numbers = [int(x) for x in input('Enter the nummber separated by spaces :').split()]
    sum = positive_sum(numbers)
    print("the sum of + intergers is :", sum)

if __name__  == "__main__":
    main()