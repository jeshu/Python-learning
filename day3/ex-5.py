# Love calculator

name_a = input('You name? ')
name_b = input('Check against? ')

name = name_a.lower() + name_b.lower()

count_l = name.count('l')
count_o = name.count('o')
count_v = name.count('v')
count_e = name.count('e')
count_t = name.count('t')
count_r = name.count('r')
count_u = name.count('u')

sum_true = count_u + count_r + count_u + count_e
sum_love = count_l + count_o + count_v + count_e

true_love = int(str(sum_true) + str(sum_love))
if true_love < 10 and true_love > 90: 
  print(f'your love score is {true_love}, you go together like coke and mentos')
elif true_love > 40 and true_love < 50:
  print(f'your love score is {true_love}, you are alright')
else :
  print(f'your love score is {true_loveBri}')
