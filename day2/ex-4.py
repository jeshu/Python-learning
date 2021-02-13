print('Welcome to the tip calculator.')
bill = float(input('what was the total bill? '))
tip = int(input('what percentage tip would you like to give ? 110, 12 or 15? '))
person = int(input('How many person to split the bill? '))


result = (bill + (bill*tip/100))/person

print(f'Each person should pay: {round(result)}')