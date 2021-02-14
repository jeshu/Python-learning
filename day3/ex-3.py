# Check leap year exercise...

year = int(input("Please enter the you want to check if its a leap year: "))

if year % 4 == 0:
  if  year % 100 != 0 :
    print('It is leap year')
  else : 
    if year % 400 == 0:
      print('It is a leap year')
    else :
      print('Not leap year')
else:
  print('Not leap year')
