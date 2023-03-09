import sys

# merge sort
def sort(target):
    # 길이가 1이면 merge를 시작하게 return 보냄
    if len(target) == 1:
        return target
    
    # list를 left, right으로 나누는 기준점
    mid = len(target) // 2
    left_target = target[:mid]
    right_target = target[mid:]
    # 쪼갠 list를 재귀로 보냄
    left_result = sort(left_target)
    right_result = sort(right_target)
    
    result = []
    i = j = 0
    # 두 list를 merge
    while i < len(left_result) and j < len(right_result):
        if left_result[i]["start"] > right_result[j]["start"] or (left_result[i]["start"] == right_result[j]["start"] and left_result[i]["end"] > right_result[j]["end"]):
            result.append(right_result[j])
            j += 1
        else:
            result.append(left_result[i])
            i += 1
    result += left_result[i:]
    result += right_result[j:]
    return result


count = int(sys.stdin.readline().rstrip())
cases = []
for i in range(count):
    value = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split()))
    cases.append(dict(start=value[0], end=value[1]))


sorted_cases = sort(cases)

# 정렬해서 반대로 뒷시간부터 시작하면 끝시간이 큰 순서대로 정렬되어있어서 뒤에서부터 해당되는 값들을 하나씩 count 하면 자연스럽게 최대 count 수와 일치함.
# start 기준으로 우선 정렬을 하기 때문에 맨 뒤의 case는 최대의 count에 포함되어있음.
total = 0
start_time = sorted_cases[-1]["start"]
for i in range(count - 1, -1, -1):
    if total == 0 or start_time >= sorted_cases[i]["end"]:
        total += 1
        start_time = sorted_cases[i]["start"]

print(total)
#count - 전체 case의 수
#cases - 입력받은 데이터
#total - 제일 높은 count 수
