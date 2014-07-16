import random

def ran5():
  return random.randrange(1,6)
  
def ranBinary():
  y = -1
  while (y == -1):
    y = ran5()/2 - 1
  return y

"""
zeros = 0
ones = 0

for x in range(0, 1000000):
  y = ranBinary()
  if y == 0:
    zeros += 1
  elif y == 1:
  	ones += 1
  else:
  	print('error: defBinary() = ' + str(y))

print("zeros: " + str(zeros))
print("ones: " + str(ones))
"""

def ran7():
  y = 0
  while y == 0:
    for x in range(0,3):
       y = y + (2**x * ranBinary())
  return y
   
results = [0,0,0,0,0,0,0]

for x in range(0, 100000):
  y = ran7()
  results[y-1] += 1
  
for x in range(0,7):
  print(str(x+1) + ": " + str(results[x]))

"""
python ~/random5to7.py 
1: 1416
2: 1420
3: 1449
4: 1437
5: 1387
6: 1450
7: 1441
"""