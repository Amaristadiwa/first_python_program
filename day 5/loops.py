#loops
 

#while loops
name = input("enter your name:")
print(name)

score = 5
while score < 10 :
    print(score)
    score = score + 1

number_to_guess = 7

guess = 7
while guess!=number_to_guess:
  guess1= int(input("guess a number:"))
  print(guess1)

if guess == number_to_guess:
    print(f"congrangulation you have guessed the correct number:")
elif guess < number_to_guess:
  print(f"too low try again")
else:
  print(f"too high try again")



answer = 7
guess = int(input("guess a number:"))

while guess != answer :
    guess = int(input("wrong number try again"))

print(f"you have guessed the correct number")