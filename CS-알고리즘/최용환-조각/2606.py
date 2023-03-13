import sys
input = sys.stdin.readline

count = int(input())
infected = [False] * count
line_count = int(input())
lines = []
for i in range(line_count):
    lines.append(list(map(int, input().split())))


def find(target):
    infected[target - 1] = True
    count = 0
    for line in lines:
        if line[0] == target and infected[line[1] - 1] == False:
            count += find(line[1]) + 1
        if line[1] == target and infected[line[0] - 1] == False:
            count += find(line[0]) + 1
    return count

print(find(1))