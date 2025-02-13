
#LeslieN
#2/11/25

#prints whether integer is divisible by 3 or 5 or both

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")

    elif i % 3 == 0:
        print("Divisible by 3")

    elif i % 5 == 0:
        print("Divisible by 5")

    else:
        print(i)
