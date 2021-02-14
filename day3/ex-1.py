# Interactive odd and even

number = int(input('Enter number you want to check for odd or event: '))

isOdd = False
if (number % 2) == 0:
  isOdd = True

if isOdd == True :
  print('Number you input is even')
else :
  print('Number you input is odd')