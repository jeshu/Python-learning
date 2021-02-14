# Pizza ordering program

print('Welcome to Python Pizza Delivery')
sizes = input('What size pizza do you want? S, M, L: ')
add_pepperoni = input('Do you want pepperoni? Y, N? ')
extra_cheese = input('Do you want extra cheese? Y, N?  ')

cost = 0
if sizes == 'L' :
  cost = 25
elif sizes == 'M' :
  cost = 20
elif sizes == 'S' :
  cost = 15

if add_pepperoni == "Y": 
  if sizes == 'S' :
    cost += 2
  else:
    cost += 3

if extra_cheese == "Y":
  cost += 1


print(f'Your final bill is: {cost}')