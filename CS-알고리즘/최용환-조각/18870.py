import sys

count = int(sys.stdin.readline().rstrip())  # 총 갯수
coords = list(sys.stdin.readline().rstrip().split())    #좌표 list
coord_set = sorted(set(coords)) #좌표 모음을 set으로 중복제거하고 정렬
indexes = {coord_set[i] : i for i in range(len(coord_set))} #좌표 index를 역으로 dict에 key를 좌표값으로 해서 보관

result = ""
for coord in coords:
    result += str(indexes[coord]) + ' '

print(result)

# list.index는 탐색할때 O(n) 이기 때문에 for 안에 넣으면 O(n^2) 라 시간복잡도 문제 생김.
# dictionary의 Key 탐색은 O(1) 이라서 활용

# import sys
# N = int(sys.stdin.readline())
# arr = list(map(int,sys.stdin.readline().split()))
# arr2 = []

# arr2 = list(sorted(set(arr)))

# dic = {arr2[i]:i for i in range (len(arr2))}

# for i in arr:
#   print(dic[i],end=' ')