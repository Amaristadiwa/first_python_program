number_to_guess = 7

print(f"welcome to the guess a number game")

guess = int(input("guess a number:"))
print(guess)

while True:
    if number_to_guess > 7:
        print("your number to guess is grater than the correct number")
        number_to_guess = int(input(f"guess another number less than{number_to_guess} :"))
    elif number_to_guess < 7:
        print("your number is less than the correct number")
        number_to_guess = int(input(f"guess another one greater than {number_to_guess} :"))
    else:
        print("you have guessed the correct number")
        number_to_guess =int(input("guess anumber :"))
