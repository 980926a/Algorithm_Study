n = int(input())
room = []

for _ in range(n):
    a,b = map(int, input().split())
    room.append([a,b])
room.sort(key= lambda x:x[1])
room.sort(key= lambda x:x[0])


print(room)

cnt = 1
end = room[0][1]
print(end)
for i in range(1,n):
    if room[i][0] >= end:
        cnt += 1
        
        end = room[i][1]
        print(end)


print(cnt)