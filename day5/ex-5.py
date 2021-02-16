# password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sp_char = ['!', '@', '#', '%', '&', '*']

print('Welcome to password generator')

nr_letters = int(input('Enter letters in password: '))
nr_numbers = int(input('Enter numbers in password: '))
nr_char = int(input('Enter symbols in password: '))

# password = ''
# for i in range(0, nr_letters):
#     password += letters[random.randint(0, len(letters)-1)]
# for j in range(0, nr_numbers):
#     password += str(numbers[random.randint(0, len(numbers)-1)])
# for k in range(0, nr_char):
#     password += sp_char[random.randint(0, len(sp_char)-1)]

# print(password)

password_list = []
for i in range(0, nr_letters):
    password_list.append(letters[random.randint(0, len(letters)-1)])
for j in range(0, nr_numbers):
    password_list.append(str(numbers[random.randint(0, len(numbers)-1)]))
for k in range(0, nr_char):
    password_list.append(sp_char[random.randint(0, len(sp_char)-1)])

random.shuffle(password_list)
pasword = ''
for p in password_list:
    pasword += p

print(pasword)
