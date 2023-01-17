N = int(input())

meeting_list = []

for i in range(N):
    meeting_start, meeting_end = map(int, input().split(' '))
    meeting_list.append((meeting_start, meeting_end))

# 한번에 key 로 정렬하는것과 값이 다르다.
meeting_list.sort(key=lambda x: (x[1],x[0]))

cnt = 0
end_time = 0

for m in meeting_list:
    if m[0] >= end_time:
        cnt += 1
        end_time = m[1]

print(cnt)