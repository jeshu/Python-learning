# Tresure island

print('Wel to the tresure island./n You misson starts now')

choice1 = input('You landed on island, want to go left of right? L, R? ')

if choice1.lower() == 'l':
  choice2 = input('You reached to river, will wait for boat of swim? boat, swim? ')
  if(choice2.lower() == 'swim') :
    choice3 = input('You reached to a chamber with two gates red and blue, which one you select? red, blue')
    if choice3.lower() == 'blue' :
      print('you got the tresure, YOU WON')
    else:
      print('Snakes came, GAME OVER')
  else :
    print('River overflowed, and you are dead, GAME OVER')
else :
  print('Monster is on the way, you are dead, GAME OVER')