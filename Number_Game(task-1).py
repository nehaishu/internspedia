import random
import math
lower_limit=int(input("Enter Lower limit for a range of numbers: "))
upper_limit=int(input("Enter upper limit for a range of numbers: "))
n = random.randint(lower_limit, upper_limit)
t=round(math.log(upper_limit - lower_limit + 1, 2))
print("\nYou've only ",t, "chances to guess the number\n")
guesses = 0
while guesses < math.log(upper_limit - lower_limit + 1, 2):
    guesses += 1
    guess = int(input("Guess the  number : "))

    if n > guess:
        print("You guessed too small!")
    elif n < guess:
        print("You guessed too high!")
    else:
        print("Congratulations! you guessed it in ", guesses, " chances.")
        break

if guesses >= math.log(upper_limit - lower_limit + 1, 2):
    print("\nThe number is %d" % n)
    print("\nBetter Luck Next time!")