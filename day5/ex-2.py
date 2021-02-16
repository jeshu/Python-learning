# High score

student_score = str(input('Enter student score: ')).split(',')

high_score = 0
for score in student_score :
  if high_score < int(score) :
    high_score = int(score)

print(f'High score is: {high_score}')