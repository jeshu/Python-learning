# Fizz Buzz

for n in range(1, 30):
    number = ''
    if n % 3 == 0:
        number += 'Fizz'
    if n % 5 == 0:
        number += 'Buzz'
    if number == '':
        number = str(n)

    print(f'{number}')
