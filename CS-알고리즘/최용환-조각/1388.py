import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
floor = []
found = []
for i in range(rows):
    row = []
    for i in range(cols):
        row.append(False)
    found.append(row)
def dfs(row, col):
    found[row][col] = True
    if floor[row][col] == '-':
        if col == cols - 1 or floor[row][col] != floor[row][col + 1]:
            return 1
        else:
            return dfs(row, col + 1)
    if floor[row][col] == '|':
        if row == rows - 1 or floor[row][col] != floor[row + 1][col]:
            return 1
        else:
            return dfs(row + 1, col)

for i in range(rows):
    row = input()
    floor.append([*row])
count = 0
for i in range(rows):
    for j in range(cols):
        if found[i][j] == True:
            continue
        count += dfs(i, j)
print(count)