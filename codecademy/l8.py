from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Guess the lucky number!: "))
  guesses_left -= 1
  if guess == random_number:
    print "You win!"
    break
else:
  print "You lose."
