x = 1
y = 2
z = 1

highNumber = 48
counter = 0

while counter < highNumber*2:
  counter += 1
  print("L", x, ".", y, "-", "P", z, sep="")
  
  if counter % 2 == 0:
    z = 1
    x += 1
  
  else:
    z = 2
