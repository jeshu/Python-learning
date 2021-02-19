# Prime numbers checkered

n = int(input('Check this number: '))


def prime_checker(number):
    isPrime = True

    if number <= 1:
        isPrime = False

    for i in range(2, number):
        if n % i == 0:
            isPrime = False

    if not isPrime:
        print('Not Prime number')
    else:
        print('Prime number')


prime_checker(number=n)
