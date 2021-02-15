# Bankers bill
import  random

name_str = input('Enter the name for all person on table: ')

name_list = name_str.split(',')
random_person = name_list[random.randint(0, len(name_list)-1)]
print(random_person+ ' will pay the bill today')