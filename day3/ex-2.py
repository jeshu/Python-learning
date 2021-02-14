## calculate the BMI

weight = int(input('Enter your weight: '))
height = int(input('Enter your height: '))

bmi = round(weight / (height ** 2))

if bmi <= 18.5 :
  print('You are underweight')
elif bmi <= 25 :
  print('You have normal weight')
elif  bmi <= 30 :
  print('You have overweight')
elif bmi < 35 :
  print('You have obese')
else  :
  print('You are clinically obese')