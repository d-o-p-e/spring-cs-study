import sys
def sort(target):
    if len(target) == 1:
        return target
    mid = len(target) // 2

    left_target = target[:mid]
    right_target = target[mid:]
    left_result = sort(left_target)
    right_result = sort(right_target)
    
    result = []
    i = j = 0
    while i < len(left_result) and j < len(right_result):
        # x 다음 y까지 정렬
        if left_result[i]["x"] > right_result[j]["x"] or (left_result[i]["x"] == right_result[j]["x"] and left_result[i]["y"] > right_result[j]["y"]):
            result.append(right_result[j])
            j += 1
        else:
            result.append(left_result[i])
            i += 1
    result += left_result[i:]
    result += right_result[j:]
    return result

count = int(sys.stdin.readline().rstrip())
dots = []
for i in range(count):
    loc = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
    dot = dict(x=loc[0], y=loc[1])
    dots.append(dot)

result = sort(dots)
for dot in result:
    print(dot["x"], dot["y"])

# count - 전체 갯수
# dots - 점 list
# result - 정렬된 점 list