
#Leslie N

#3/16/25

#Problem 3
#Get user input and create a list until it adds up to 100

numbers = []
total_sum = 0


while total_sum <= 100:
    number = float(input("Enter a number: "))
    numbers.append(number)
    total_sum += number


print("Numbers entered:", numbers)
print("Total sum:", total_sum)
