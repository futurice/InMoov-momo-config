def turnhead(coords):
  i01.startedGesture()

  i01.setHeadSpeed(0.6, 0.6)

  global globneck
  global globrot

  # x and y coordinates on the dashboard 100x100 grid
  lcoords = coords.split('/')
  x = int(lcoords[0])
  y = int(lcoords[1])

  # need to flip them as the grid is in opposite alignment
  rothead = round(100 - x) 
  neck = round(100 - y)

  # our field of vision is 70 degrees, so we want x of -35 to 35
  rothead = int(rothead) * 0.7 - 35

  # the absolute position is old x plus the delta
  rothead = int(globrot) + int(rothead)

  if rothead > 180 :
    rothead = 180

  if rothead < 0 :
    rothead = 0

  # talk("rot on " + str(rothead))

  i01.moveHead(neck, rothead)

  # store the new value into the global variable
  globrot = rothead

  i01.head.rothead.setVelocity(100)
  i01.head.neck.setVelocity(100)

  i01.finishedGesture()
