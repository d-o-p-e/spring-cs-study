# sorting by merge sort
def sort_desc(target):
    if len(target) == 1:
        return target
    mid = len(target) // 2

    left_target = target[:mid]
    right_target = target[mid:]
    left_result = sort_desc(left_target)
    right_result = sort_desc(right_target)
    
    result = []
    i = j = 0
    while i < len(left_result) and j < len(right_result):
        if left_result[i] < right_result[j]:
            result.append(right_result[j])
            j += 1
        else:
            result.append(left_result[i])
            i += 1
    result += left_result[i:]
    result += right_result[j:]
    return result

result = 0
count = int(input())

times = []
times = list(map(lambda x: int(x), input().split(" ")))
times = sort_desc(times)

for i in range(count, 0, -1):
    result += i * times[i - 1]
print(result)

# count - 전체 개수
# times - 각 사람의 시간