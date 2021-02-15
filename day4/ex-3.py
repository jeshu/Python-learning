row1 = ['#','#','#']
row2 = ['#','#','#']
row3 = ['#','#','#']
board = [row1, row2, row3]

print(row1)
print(row2)
print(row3)
positions = str(input('Where you want to place tresure: '))

row = board[int(positions[0])-1]
row[int(positions[1])-1] = 'X' 

print(row1)
print(row2)
print(row3)