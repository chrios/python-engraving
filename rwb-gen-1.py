counter = 0
rwbCount = 0

maxNumber = int(input("Enter the max number: "))

while counter < maxNumber:
  
  rwbCount += 1
  counter +=1
  
  if rwbCount == 1:
    rwb = 'R'
    
  if rwbCount == 2:
    rwb = 'W'
    
  if rwbCount == 3:
    rwb = 'B'
    rwbCount = 0
    
  print(rwb, counter, sep='')
