i = int(input("Enter the number :"))

for j in range(2,i):
    if i % j == 0:
        print("Not a prime number!!!")
        break
else:
    print("Prime!!!")