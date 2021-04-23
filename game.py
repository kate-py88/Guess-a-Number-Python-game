import random

hidden = random.randrange(1,201)
print(hidden)

num = int(input("Please, enter your number"))

if num == hidden :
    print("You win! :D")
elif num < hidden :
    print("Your number is lower than the hidden one")
else :
    print("Your number is greater than the hidden")