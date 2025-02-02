
#LeslieN
#02/01/25

#give day of week you return from trip

startday = float(input("What is your starting day number? "))

lengthstay = float(input("How long is your stay? "))

total = startday + lengthstay

returnday = total % 7

print("You will return on day ", returnday)

