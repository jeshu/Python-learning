# Hangman
import random


def draw_hangman() :
  print('Hangman')

word_list = ['ardvark', 'baboon', 'camel']

word = random.choice(word_list)

print('selected word is: ' + word)
display = []
for s in word :
  display += '_'

print(f' The word is : {display}')
life = len(word)
game_over = False
while not game_over :
  guess_letter = str(input('Guess the letter:')).lower()

  for i in range(len(word)) :
    letter = word[i]
    if letter == guess_letter :
      display[i] = letter
  
  print(f'life remaining {life} \n {display}')
  if guess_letter not in word :
    print('Wrong choice -- a life lost')
    life -= 1

  if '_' not in display or life < 1:
    print('Game over')
    if life >= 1 :
      print('you win')
    game_over = True
    