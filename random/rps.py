import random
lst = ['rock', 'paper', 'scissors']
answer = input("Choose rock, paper, or scissors: ").lower()
against = random.choice(lst)
while answer not in lst:
    answer = input("Please, be reasonable and choose rock, paper, or scissors: ")
print("You chose " + answer + " and computer chose " + against)
if answer == against:
    print("It's a draw!")
    result = 'drew'
elif answer == 'scissors' and against == 'rock':
    print("You lose!")
    result = 'lost'
elif answer == 'paper' and against == 'scissors':
    print("You lose!")
    result = 'lost'
elif answer == 'rock' and against == 'paper':
    print("You lose!")
    result = 'lost'
elif answer == 'rock' and against == 'scissors':
    print("You win!")
    result = 'won'
elif answer == 'scissors' and against == 'paper':
    print("You win!")
    result = 'won'
elif answer == 'paper' and against == 'rock':
    print("You win!")
    result = 'won'
with open('./results.txt', 'a') as out:
    out.write('computer chose ' + against + '\n' + 'player chose ' + answer + '\n' + 'player ' + result + '\n')
