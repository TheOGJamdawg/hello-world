import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
max_guesses = math.ceil(math.log2(larger - smaller + 1))
count = 0
print("Think of a number between", smaller, "and", larger, ". I will guess within", max_guesses, "tries.")

while count < max_guesses:
    guess = round((smaller + larger) / 2)
    count += 1
    print("My guess is",guess,)
    feedback = input("Press h for too high, l for too low, or c for a correct guess: ")

    if feedback == 'c':
        print("I got it right! It took me", count, "tries!")
        break
    elif feedback == 'h':
        larger = guess - 1
    elif feedback == 'l':
        smaller = guess + 1
    else:
        print("Please only use 'h', 'l', or 'c'")
        count -= 1
        continue

    if smaller > larger or larger < smaller:
        print("You seem to be giving me misleading information")
        break
else:
    print("Did you forget your number?")
    
