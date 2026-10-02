
number = 9

print("Guess the number between 0 and 9")

while True:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break