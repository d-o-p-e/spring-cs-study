import sys
input = sys.stdin.readline
size = int(input())
searched = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(False)
    searched.append(row)
area = []
for i in range(size):
    line = input()
    area.append([*line])

def find(row, col):
    searched[row][col] = True
    count = 1
    if col < size - 1 and area[row][col + 1] == '1' and searched[row][col + 1] == False:
        count += find(row, col + 1)
    if col != 0 and area[row][col - 1] == '1' and searched[row][col - 1] == False:
        count += find(row, col - 1)
    if row < size - 1 and area[row + 1][col] == '1' and searched[row + 1][col] == False:
        count += find(row + 1, col)
    if row != 0 and area[row - 1][col] == '1' and searched[row - 1][col] == False:
        count += find(row - 1, col)
    return count

total = 0
cases = []
for row in range(size):
    for col in range(size):
        if area[row][col] == '0' or searched[row][col] == True:
            continue
        total += 1
        cases.append(find(row, col))
print(total)
for case in sorted(cases):
    print(case)