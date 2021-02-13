## calculate the BMI

weight = int(input('Enter your weight: '))
height = int(input('Enter your height: '))

bmi = weight / (height ** 2)

print('your BMI is : ' + str(bmi))