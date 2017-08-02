from random import randint
number=randint(0,100)
while True:
    guess=int(input("Enter your guess between 0 to 100"+"/n"))

    if guess==number:
        print("Your guess is correct the number is"+str(number))
        break
    elif guess < number:
        print("The number is greater than your guess")
    else:
        print("The number is less than your guess")
