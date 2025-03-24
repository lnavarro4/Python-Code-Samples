
#Leslie N

#3/16/25

#Problem 4
#Add multiples of 10 to list

counter = 0
tens = []

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1


print("Multiples of 10:", tens)
