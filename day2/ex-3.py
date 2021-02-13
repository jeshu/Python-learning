# Life remaining output

age = int(input('What is your age: '));

days_left = int((90 - age) * 365)
weeks_left = int(days_left / 7)
months_left = int( (90-age) * 12)

print(f'You have left {days_left} days, {weeks_left} weeks and {months_left} months left.')