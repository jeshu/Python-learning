# Student height avg

student_height = str(input('input the students hight: ')).split((','))

sum_hight = 0
counter = 0
for student in student_height :
  counter += 1
  sum_hight += int(student)

avg = sum_hight/counter
print(f'avg student height is {avg}')