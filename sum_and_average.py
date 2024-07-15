def calculate_sum_and_average(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    average = total_sum / len(numbers)
    return total_sum, average

# Taking input from the user
numbers_list = []
num_count = int(input("Enter the number of elements in the list: "))
print("Enter the elements:")
for i in range(num_count):
    num = float(input())
    numbers_list.append(num)

total_sum, average = calculate_sum_and_average(numbers_list)

print("Sum:", total_sum)
print("Average:", average)



