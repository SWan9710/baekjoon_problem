N = int(input())

meeting_room = []
for i in range(N):
    meeting_time = list(map(int, input().split()))
    meeting_room.append(meeting_time)

print(meeting_room)

count = 1
for i in range(N-1):
    for j in range(1,N):
        if i >= j:
            continue
        if meeting_room[i][-1] <= meeting_room[j][0]:
            count += 1
            print(meeting_room[j][0])
            break
    

print(count)
