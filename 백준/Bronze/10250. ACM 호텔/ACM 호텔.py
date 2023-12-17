t = int(input())
for i in range(t) :
  h,w,n = map(int,input().split())
  hlst = [i for i in range(1,h+1)]
  wlst = [i for i in range(1,w+1)]
  hotel = []
  cnt = 0
  for j in range(1,len(wlst)+1) :
    for i in range(1,len(hlst)+1) :
      cnt += 1
      room_number = f"{i}{j:02d}"
      hotel.append(room_number)
      if n == cnt :
        print(room_number)

