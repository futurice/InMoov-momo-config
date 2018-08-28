def turnheaddirection(dir):
  i01.startedGesture()

  i01.setHeadSpeed(0.6, 0.6)

  global globneck
  global globrot

  rothead = globrot
  neck = globneck

  if dir == 'up':
    neck = neck + 5

  if dir == 'right':
    rothead = rothead - 5

  if dir == 'down':
    neck = neck - 5

  if dir == 'left':
    rothead = rothead + 5

  if rothead > 180 :
    rothead = 180

  if rothead < 0 :
    rothead = 0

  if neck < 0 :
    neck = 0
  
  if neck > 180 :
    neck = 180

  i01.moveHead(neck, rothead)

  # store the new value into the global variable
  globrot = rothead
  globneck = neck

  i01.head.rothead.setVelocity(100)
  i01.head.neck.setVelocity(100)

  i01.finishedGesture()
