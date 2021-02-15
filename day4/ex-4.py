import random

rock = 'ROCK'
paper = 'PAPER'
sissors = 'SISSORS'
computer_moves = [[paper, sissors], [sissors, rock], [rock, paper]]

pl = input("Select your move: r,s,p ? ")


if pl == 's':
  autoMove = computer_moves[2][random.randint(0,1)]
  if autoMove == paper :
    print('Computer move '+ paper +', you WIN')
  else:
    print('Computer move '+rock  +', you LOST')  
elif pl == 'r':
  autoMove = computer_moves[0][random.randint(0,1)]
  if autoMove == sissors :
    print('Computer move '+sissors +', you WIN')
  else:
    print('Computer move '+paper +', you LOST')  
elif pl == 'p':
  autoMove = computer_moves[1][random.randint(0,1)]
  if autoMove == rock :
    print('Computer move '+rock +', you WIN')
  else:
    print('Computer move '+sissors+', you LOST')  
