xPos = [ None ] * 16
yPos = [ None ] * 16
zPos = [ None ] * 16

data = []
for el in range(27):
    data.append(el)

evt_cnt = 0

for z in range(3):
   zPos[z] = z
   for y in range(3):
       for x in range(3):
           xPos[x] = x
           yPos[y] = y
           print evt_cnt, data[evt_cnt]
           evt_cnt += 1

